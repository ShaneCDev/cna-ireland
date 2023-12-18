from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=256)
    friendly_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=256, unique=True, null=False)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    review_date = models.DateTimeField(default=timezone.now)
    scores = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    stars = models.IntegerField(choices=scores, default=1)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    comment = models.TextField(max_length=3000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['created_on']
    
    def __str__(self):
        return f'Review by {self.author}'