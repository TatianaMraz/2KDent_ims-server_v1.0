# Generated by Django 5.0.3 on 2024-04-26 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_product_stock_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock_location',
        ),
        migrations.AddField(
            model_name='product',
            name='stock_number',
            field=models.CharField(default='Číslo skladu', max_length=100),
        ),
    ]
