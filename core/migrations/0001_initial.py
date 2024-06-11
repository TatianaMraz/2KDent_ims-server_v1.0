# Generated by Django 5.0.3 on 2024-06-11 11:11

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=255)),
                ('order_number', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('is_delivered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TableHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Název', max_length=100)),
                ('stock_number', models.CharField(default='Číslo skladu', max_length=100)),
                ('order_number', models.CharField(default='Číslo obj.', max_length=100)),
                ('quantity', models.CharField(default='Množství', max_length=100)),
                ('min_quantity', models.CharField(default='Min. množství', max_length=100)),
                ('expiration_date', models.CharField(default='Expirace', max_length=100)),
                ('supplier', models.CharField(default='Dodavatel', max_length=100)),
                ('order_date', models.CharField(default='Datum objednání', max_length=100)),
                ('delivery_date', models.CharField(default='Datum dodání', max_length=100)),
                ('note', models.CharField(default='Poznámka', max_length=100)),
                ('is_delivered', models.CharField(default='Dodáno', max_length=100)),
                ('address', models.CharField(default='Adresa', max_length=100)),
                ('bank_account', models.CharField(default='Bank. účet', max_length=100)),
                ('company', models.CharField(default='Firma', max_length=100)),
                ('contact', models.CharField(default='Kontakt', max_length=100)),
                ('dic', models.CharField(default='DIČ', max_length=100)),
                ('ico', models.CharField(default='IČO', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('min_quantity', models.PositiveIntegerField(default=1)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('supplier', models.CharField(max_length=255)),
                ('product_type', models.CharField(choices=[('Materiál', 'Materiál'), ('Nástroj', 'Nástroj'), ('Zařízení', 'Zařízení')], default='Materiál', max_length=20)),
                ('note', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_files/')),
                ('stock_number', models.CharField(default='Centrální sklad', max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('ico', models.CharField(max_length=10)),
                ('dic', models.CharField(blank=True, max_length=10, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier_updated_by', to=settings.AUTH_USER_MODEL)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
