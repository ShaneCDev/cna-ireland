# Generated by Django 4.2.3 on 2023-12-08 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productreview_stars'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'Reviews'},
        ),
    ]
