# Generated by Django 5.0.3 on 2024-04-11 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_image_alter_product_product_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='minimum_quantity',
            new_name='min_quantity',
        ),
    ]