# Generated by Django 5.0.3 on 2024-04-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_product_stock_location_product_stock_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_number',
            field=models.CharField(default='Centrální sklad', max_length=100),
        ),
    ]
