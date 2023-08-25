from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_date = models.DateField(auto_now_add=True, null=True)
    comment = models.TextField(max_length=4000)

    class Meta:
        ordering = ['blog_date']

    def __str__(self):
        return f'Blog { self.comment } by { self.author }'
