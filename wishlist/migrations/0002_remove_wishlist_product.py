# Generated by Django 4.2.3 on 2024-01-04 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
    ]
