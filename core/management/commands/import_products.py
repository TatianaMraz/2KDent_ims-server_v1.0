from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.utils.dateparse import parse_date

from accounts.models import CustomUser
from core.models import Supplier, Product, Manufacturer, SupplierSet


class Command(BaseCommand):
    help = 'Import products into the database'

    def handle(self, *args, **kwargs):
        default_user = CustomUser.objects.get(username='npgroup-admin')

        product_data = [
            {
                'name': 'Dental Cement',
                'quantity': 100,
                'min_quantity': 10,
                'expiration_date': '2025-12-31',
                'product_type': 'Materiál',
                'stock_number': 'Lokace 1',
                'note': 'High strength, suitable for crowns.',
                'supplier_set': [
                    {"supplier": 1, "manufacturer": 2},
                    {"supplier": 12, "manufacturer": 5}
                ]
            },
            {
                'name': 'Dental Mirror',
                'quantity': 50,
                'min_quantity': 5,
                'expiration_date': '2028-06-30',
                'product_type': 'Nástroj',
                'stock_number': 'Centrální sklad',
                'note': 'Anti-fog coating.',
                'supplier_set': [
                    {"supplier": 3, "manufacturer": 4}
                ]
            },
            {
                'name': 'Composite Resin',
                'quantity': 200,
                'min_quantity': 20,
                'expiration_date': '2024-11-15',
                'product_type': 'Materiál',
                'stock_number': 'Centrální sklad',
                'note': 'Ideal for aesthetic restorations.',
                'supplier_set': [
                    {"supplier": 5, "manufacturer": 6}
                ]
            },
            {
                'name': 'Dental Drill',
                'quantity': 30,
                'min_quantity': 3,
                'expiration_date': '2027-03-10',
                'product_type': 'Nástroj',
                'stock_number': 'Centrální sklad',
                'note': 'High-speed stainless steel drill.',
                'supplier_set': [
                    {"supplier": 7, "manufacturer": 8}
                ]
            },
            {
                'name': 'Ultrasonic Scaler',
                'quantity': 10,
                'min_quantity': 2,
                'expiration_date': '2029-09-20',
                'product_type': 'Zařízení',
                'stock_number': 'Centrální sklad',
                'note': 'Efficient plaque and tartar removal.',
                'supplier_set': [
                    {"supplier": 9, "manufacturer": 10}
                ]
            },
            {
                'name': 'Dental Forceps',
                'quantity': 40,
                'min_quantity': 4,
                'expiration_date': '2030-01-01',
                'product_type': 'Nástroj',
                'stock_number': 'Centrální sklad',
                'note': 'Ergonomic handle design.',
                'supplier_set': [
                    {"supplier": 11, "manufacturer": 12}
                ]
            },
            {
                'name': 'Dental Floss',
                'quantity': 500,
                'min_quantity': 50,
                'expiration_date': '2026-08-08',
                'product_type': 'Materiál',
                'stock_number': 'Centrální sklad',
                'note': 'Mint flavored for fresh breath.',
                'supplier_set': [
                    {"supplier": 13, "manufacturer": 14}
                ]
            },
            {
                'name': 'Amalgam Capsule',
                'quantity': 150,
                'min_quantity': 15,
                'expiration_date': '2025-07-22',
                'product_type': 'Materiál',
                'stock_number': 'Centrální sklad',
                'note': 'Long-lasting, mercury alloy.',
                'supplier_set': [
                    {"supplier": 2, "manufacturer": 1}
                ]
            },
            {
                'name': 'LED Curing Light',
                'quantity': 20,
                'min_quantity': 2,
                'expiration_date': '2031-02-18',
                'product_type': 'Zařízení',
                'stock_number': 'Centrální sklad',
                'note': 'Wireless, fast curing.',
                'supplier_set': [
                    {"supplier": 4, "manufacturer": 3}
                ]
            },
            {
                'name': 'Dental Bib',
                'quantity': 1000,
                'min_quantity': 100,
                'expiration_date': '2025-05-25',
                'product_type': 'Materiál',
                'stock_number': 'Lokace 1',
                'note': 'Waterproof, single-use.',
                'supplier_set': [
                    {"supplier": 6, "manufacturer": 5}
                ]
            },
            {
                'name': 'Impression Tray',
                'quantity': 80,
                'min_quantity': 8,
                'expiration_date': '2028-12-30',
                'product_type': 'Nástroj',
                'stock_number': 'Centrální sklad',
                'note': 'Adjustable, reusable.',
                'supplier_set': [
                    {"supplier": 8, "manufacturer": 7}
                ]
            },
            {
                'name': 'Prophy Paste',
                'quantity': 300,
                'min_quantity': 30,
                'expiration_date': '2026-10-10',
                'product_type': 'Materiál',
                'stock_number': 'Lokace 2',
                'note': 'Grit for polishing teeth.',
                'supplier_set': [
                    {"supplier": 10, "manufacturer": 9}
                ]
            },
            {
                'name': 'Root Canal File',
                'quantity': 70,
                'min_quantity': 7,
                'expiration_date': '2027-07-04',
                'product_type': 'Nástroj',
                'stock_number': 'Centrální sklad',
                'note': 'Flexible, stainless steel.',
                'supplier_set': [
                    {"supplier": 12, "manufacturer": 11}
                ]
            },
            {
                'name': 'Dental Handpiece',
                'quantity': 25,
                'min_quantity': 2,
                'expiration_date': '2029-11-11',
                'product_type': 'Zařízení',
                'stock_number': 'Centrální sklad',
                'note': 'High-torque, lightweight.',
                'supplier_set': [
                    {"supplier": 14, "manufacturer": 13}
                ]
            },
            {
                'name': 'Orthodontic Bracket',
                'quantity': 500,
                'min_quantity': 50,
                'expiration_date': '2028-03-03',
                'product_type': 'Materiál',
                'stock_number': 'Centrální sklad',
                'note': 'Stainless steel, strong bond.',
                'supplier_set': [
                    {"supplier": 1, "manufacturer": 2}
                ]
            },
            {
                'name': 'Dental Tray Paper',
                'quantity': 2000,
                'min_quantity': 200,
                'expiration_date': '2025-06-15',
                'product_type': 'Materiál',
                'stock_number': 'Lokace 1',
                'note': 'Absorbent, single-use.',
                'supplier_set': [
                    {"supplier": 3, "manufacturer": 4}
                ]
            },
            {
                'name': 'Disposable Syringe',
                'quantity': 1000,
                'min_quantity': 100,
                'expiration_date': '2026-01-01',
                'product_type': 'Materiál',
                'stock_number': 'Centrální sklad',
                'note': 'Sterile, single-use.',
                'supplier_set': [
                    {"supplier": 5, "manufacturer": 6}
                ]
            },
            {
                'name': 'Dental X-ray Sensor',
                'quantity': 15,
                'min_quantity': 2,
                'expiration_date': '2031-04-04',
                'product_type': 'Zařízení',
                'stock_number': 'Lokace 2',
                'note': 'High-resolution imaging.',
                'supplier_set': [
                    {"supplier": 7, "manufacturer": 8}
                ]
            },
            {
                'name': 'Dental Articulator',
                'quantity': 35,
                'min_quantity': 3,
                'expiration_date': '2030-12-12',
                'product_type': 'Zařízení',
                'stock_number': 'Centrální sklad',
                'note': 'Adjustable, accurate simulations.',
                'supplier_set': [
                    {"supplier": 9, "manufacturer": 10}
                ]
            },
            {
                'name': 'Dental Spatula',
                'quantity': 60,
                'min_quantity': 6,
                'expiration_date': '2027-05-05',
                'product_type': 'Nástroj',
                'stock_number': 'Lokace 2',
                'note': 'Stainless steel, non-stick surface.',
                'supplier_set': [
                    {"supplier": 11, "manufacturer": 12}
                ]
            }
        ]

        # Delete all rows from the Product table
        Product.objects.all().delete()

        # Reset autoincrement to start with id 1
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='core_product';")

        with transaction.atomic():
            # Delete all rows from the Product table
            Product.objects.all().delete()

            for data in product_data:
                # Parse expiration_date string into a date object
                expiration_date_str = data.pop('expiration_date')
                expiration_date = parse_date(expiration_date_str)

                # Extract supplier_set from data and remove from data dictionary
                supplier_set_data = data.pop('supplier_set', [])

                # Create product instance
                product = Product(**data, expiration_date=expiration_date, created_by=default_user)
                product.save()

                # Create SupplierSet instances
                for supplier_data in supplier_set_data:
                    supplier_id = supplier_data.get('supplier')
                    manufacturer_id = supplier_data.get('manufacturer')

                    supplier = Supplier.objects.get(pk=supplier_id)
                    manufacturer = Manufacturer.objects.get(pk=manufacturer_id)

                    SupplierSet.objects.create(product=product, supplier=supplier, manufacturer=manufacturer)

        self.stdout.write(self.style.SUCCESS('Products imported successfully.'))

