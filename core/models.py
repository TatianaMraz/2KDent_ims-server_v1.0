from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class Table(models.Model):
    title = models.CharField(max_length=100)


class TableHead(models.Model):
    name = models.CharField(max_length=100, default='Název')
    stock_number = models.CharField(max_length=100, default='Číslo skladu')
    order_number = models.CharField(max_length=100, default='Číslo obj.')
    quantity = models.CharField(max_length=100, default='Množství')
    min_quantity = models.CharField(max_length=100, default='Min. množství')
    expiration_date = models.CharField(max_length=100, default='Expirace')
    supplier = models.CharField(max_length=100, default='Dodavatel')
    status = models.CharField(max_length=100, default='Status')
    order_date = models.CharField(max_length=100, default='Datum objednání')
    delivery_date = models.CharField(max_length=100, default='Datum dodání')


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    min_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    expiration_date = models.DateField(null=True, blank=True)
    supplier = models.CharField(max_length=255)
    product_type_choices = [
        ('Materiál', 'Materiál'),
        ('Nástroj', 'Nástroj'),
        ('Zařízení', 'Zařízení'),
    ]
    product_type = models.CharField(max_length=20, choices=product_type_choices, default='Materiál')
    image = models.ImageField(upload_to='product_files/', null=True, blank=True)
    note = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.expiration_date and self.expiration_date < timezone.now().date():
            raise ValidationError({'expiration_date': ['Datum expirace nemůže být v minulosti.']})
        super().save(*args, **kwargs)


class Order(models.Model):
    name = models.CharField(max_length=100, default='Název položky')
    supplier = models.CharField(max_length=255)
    order_no = models.CharField(max_length=100, default='Číslo objednávky')
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.delivery_date and self.delivery_date < timezone.now().date():
            raise ValidationError({'delivery_date': ['Datum dodání nemůže být v minulosti.']})
        super().save(*args, **kwargs)



