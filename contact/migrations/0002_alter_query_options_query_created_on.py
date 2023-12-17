# Generated by Django 4.2.3 on 2023-12-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='query',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'Queries'},
        ),
        migrations.AddField(
            model_name='query',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]