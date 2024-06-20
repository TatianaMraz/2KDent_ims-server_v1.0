from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class Table(models.Model):
    title = models.CharField(max_length=100)


class TableHead(models.Model):
    name = models.CharField(max_length=100, default='Název')
    supplier = models.CharField(max_length=100, default='Dodavatel')
    quantity = models.CharField(max_length=100, default='Množství')
    min_quantity = models.CharField(max_length=100, default='Min. množství')
    expiration_date = models.CharField(max_length=100, default='Expirace')
    order_date = models.CharField(max_length=100, default='Datum objednání')
    delivery_date = models.CharField(max_length=100, default='Datum dodání')
    is_delivered = models.CharField(max_length=100, default='Dodáno')
    order_number = models.CharField(max_length=100, default='Číslo obj.')
    stock_number = models.CharField(max_length=100, default='Číslo skladu')
    note = models.CharField(max_length=100, default='Poznámka')
    company = models.CharField(max_length=100, default='Firma')
    address = models.CharField(max_length=100, default='Adresa')
    ico = models.CharField(max_length=100, default='IČO')
    dic = models.CharField(max_length=100, default='DIČ')
    bank_account = models.CharField(max_length=100, default='Bank. účet')
    contact = models.CharField(max_length=100, default='Kontakt')


class Supplier(models.Model):
    company = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    ico = models.CharField(max_length=10)
    dic = models.CharField(max_length=10, blank=True, null=True)
    bank_account = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='supplier_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='supplier_updated_by', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Manufacturer(models.Model):
    company = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    ico = models.CharField(max_length=20)
    dic = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='manufacturer_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='manufacturer_updated_by', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField(default=1)
    min_quantity = models.PositiveIntegerField(default=1)
    expiration_date = models.DateField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    PRODUCT_TYPE_CHOICES = [
        ('Materiál', 'Materiál'),
        ('Nástroj', 'Nástroj'),
        ('Zařízení', 'Zařízení'),
    ]
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES, default='Materiál')
    stock_number = models.CharField(max_length=100, default='Centrální sklad')
    image = models.ImageField(upload_to='product_files/', null=True, blank=True)
    note = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='created_by', null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='updated_by', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.expiration_date and self.expiration_date < timezone.now().date():
            raise ValidationError({'expiration_date': ['Datum expirace nemůže být v minulosti.']})
        super().save(*args, **kwargs)


class Order(models.Model):
    name = models.CharField(max_length=100)
    supplier = models.CharField(max_length=255)
    order_number = models.CharField(max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    is_delivered = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.delivery_date and self.delivery_date < timezone.now().date():
            raise ValidationError({'delivery_date': ['Datum dodání nemůže být v minulosti.']})
        super().save(*args, **kwargs)



