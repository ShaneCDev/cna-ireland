from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class WishlistItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.product.name}'


class Wishlist(models.Model):
    owner = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    wishlist = models.ManyToManyField(WishlistItem)

    def __str__(self):
        return f"{self.owner}'s wishlist"