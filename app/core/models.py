from django.db import models


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