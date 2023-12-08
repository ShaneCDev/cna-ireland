from django.db import models
from django.contrib.auth.models import User


class Query(models.Model):

    class Meta:
        verbose_name_plural = 'Queries'
        ordering = ['created_on']
    
    email = models.EmailField(max_length=256, blank=False, null=False)
    subject = models.CharField(max_length=256, null=False, blank=False)
    message = models.TextField(max_length=4000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Query from {self.email}'