# Generated by Django 5.0.3 on 2024-07-20 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_product_stock_number_stock_delete_productstore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]