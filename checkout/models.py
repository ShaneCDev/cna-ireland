import uuid
from datetime import datetime
from django.db.models import Sum
from django.db import models
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.code} - {self.discount_percent}% discount'


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(null=True)
    order_datetime = models.DateTimeField(null=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    discount_code = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-order_datetime']

    def _generate_order_number(self):
        """
        Generate order number using UUID
        """
        return uuid.uuid4().hex.upper()[:8]


    def update_total(self):
        """
        Update the grand total each time a new item is added to the order
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        if self.date and self.order_time:
            self.order_datetime = datetime.combine(self.date, self.order_time)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override save method to set order number
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
