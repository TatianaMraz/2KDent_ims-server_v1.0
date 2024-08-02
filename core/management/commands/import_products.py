from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.utils.dateparse import parse_date

from accounts.models import CustomUser
from core.models import Supplier, Product, Manufacturer, SupplierSet, Store, Stock


class Command(BaseCommand):
    help = 'Import products into the database'

    def handle(self, *args, **kwargs):
        default_user = CustomUser.objects.get(username='npgroup-admin')

        product_data = [
            {
                'name': 'Dental Cement',
                'min_quantity': 10,
                'expiration_date': '2024-08-30',
                'product_type': 'Materiál',
                'note': 'High strength, suitable for crowns.',
                'supplier_set': [
                    {"supplier": 1, "manufacturer": 2},
                    {"supplier": 12, "manufacturer": 5}
                ],
                'stock': [
                    {"store": 1, "quantity": 5},
                    {"store": 2, "quantity": 0},
                    {"store": 3, "quantity": 2},
                ]
            },
            {
                'name': 'Dental Mirror',
                'min_quantity': 5,
                'expiration_date': '2024-07-20',
                'product_type': 'Nástroj',
                'note': 'Anti-fog coating.',
                'supplier_set': [
                    {"supplier": 3, "manufacturer": 4}
                ],
                'stock': [
                    {"store": 1, "quantity": 3},
                    {"store": 2, "quantity": 1},
                    {"store": 3, "quantity": 0},
                ]
            },
            {
                'name': 'Composite Resin',
                'min_quantity': 20,
                'expiration_date': '2024-07-30',
                'product_type': 'Materiál',
                'note': 'Ideal for aesthetic restorations.',
                'supplier_set': [
                    {"supplier": 5, "manufacturer": 6}
                ],
                'stock': [
                    {"store": 1, "quantity": 70},
                    {"store": 2, "quantity": 0},
                    {"store": 3, "quantity": 0},
                ]
            },
            {
                'name': 'Dental Drill',
                'min_quantity': 15,
                'expiration_date': '2027-03-10',
                'product_type': 'Nástroj',
                'note': 'High-speed stainless steel drill.',
                'supplier_set': [
                    {"supplier": 7, "manufacturer": 8}
                ],
                'stock': [
                    {"store": 1, "quantity": 4},
                    {"store": 2, "quantity": 15},
                    {"store": 3, "quantity": 0},
                ]
            },
            {
                'name': 'Ultrasonic Scaler',
                'min_quantity': 2,
                'expiration_date': '2029-09-20',
                'product_type': 'Zařízení',
                'note': 'Efficient plaque and tartar removal.',
                'supplier_set': [
                    {"supplier": 9, "manufacturer": 10}
                ],
                'stock': [
                    {"store": 1, "quantity": 0},
                    {"store": 2, "quantity": 35},
                    {"store": 3, "quantity": 15}
                ]
            },
            {
                'name': 'Dental Forceps',
                'min_quantity': 4,
                'expiration_date': '2030-01-01',
                'product_type': 'Nástroj',
                'note': 'Ergonomic handle design.',
                'supplier_set': [
                    {"supplier": 11, "manufacturer": 12}
                ],
                'stock': [
                    {"store": 1, "quantity": 50},
                    {"store": 2, "quantity": 0},
                    {"store": 3, "quantity": 30}
                ]
            },
            {
                'name': 'Dental Floss',
                'min_quantity': 50,
                'expiration_date': '2026-08-08',
                'product_type': 'Materiál',
                'note': 'Mint flavored for fresh breath.',
                'supplier_set': [
                    {"supplier": 13, "manufacturer": 14}
                ],
                'stock': [
                    {"store": 1, "quantity": 0},
                    {"store": 2, "quantity": 8},
                    {"store": 3, "quantity": 70}
                ]
            },
            {
                'name': 'Amalgam Capsule',
                'min_quantity': 15,
                'expiration_date': '2025-07-22',
                'product_type': 'Materiál',
                'note': 'Long-lasting, mercury alloy.',
                'supplier_set': [
                    {"supplier": 2, "manufacturer": 1}
                ],
                'stock': [
                    {"store": 1, "quantity": 60},
                    {"store": 2, "quantity": 0},
                    {"store": 3, "quantity": 90}
                ]
            },
            {
                'name': 'LED Curing Light',
                'min_quantity': 30,
                'expiration_date': '2031-02-18',
                'product_type': 'Zařízení',
                'note': 'Wireless, fast curing.',
                'supplier_set': [
                    {"supplier": 4, "manufacturer": 3}
                ],
                'stock': [
                    {"store": 1, "quantity": 21},
                    {"store": 2, "quantity": 16},
                    {"store": 3, "quantity": 0},
                ]
            },
            # {
            #     'name': 'Dental Bib',
            #     'quantity': 1000,
            #     'min_quantity': 100,
            #     'expiration_date': '2025-05-25',
            #     'product_type': 'Materiál',
            #     'stock_number': 'Lokace 1',
            #     'note': 'Waterproof, single-use.',
            #     'supplier_set': [
            #         {"supplier": 6, "manufacturer": 5}
            #     ]
            # },
            # {
            #     'name': 'Impression Tray',
            #     'quantity': 80,
            #     'min_quantity': 8,
            #     'expiration_date': '2028-12-30',
            #     'product_type': 'Nástroj',
            #     'stock_number': 'Centrální sklad',
            #     'note': 'Adjustable, reusable.',
            #     'supplier_set': [
            #         {"supplier": 8, "manufacturer": 7}
            #     ]
            # },
            # {
            #     'name': 'Prophy Paste',
            #     'quantity': 300,
            #     'min_quantity': 30,
            #     'expiration_date': '2026-10-10',
            #     'product_type': 'Materiál',
            #     'stock_number': 'Lokace 2',
            #     'note': 'Grit for polishing teeth.',
            #     'supplier_set': [
            #         {"supplier": 10, "manufacturer": 9}
            #     ]
            # },
            # {
            #     'name': 'Root Canal File',
            #     'quantity': 70,
            #     'min_quantity': 7,
            #     'expiration_date': '2027-07-04',
            #     'product_type': 'Nástroj',
            #     'stock_number': 'Centrální sklad',
            #     'note': 'Flexible, stainless steel.',
            #     'supplier_set': [
            #         {"supplier": 12, "manufacturer": 11}
            #     ]
            # },
            # {
            #     'name': 'Dental Handpiece',
            #     'quantity': 25,
            #     'min_quantity': 2,
            #     'expiration_date': '2029-11-11',
            #     'product_type': 'Zařízení',
            #     'stock_number': 'Centrální sklad',
            #     'note': 'High-torque, lightweight.',
            #     'supplier_set': [
            #         {"supplier": 14, "manufacturer": 13}
            #     ]
            # },
            # {
            #     'name': 'Orthodontic Bracket',
            #     'quantity': 500,
            #     'min_quantity': 50,
            #     'expiration_date': '2028-03-03',
            #     'product_type': 'Materiál',
            #     'stock_number': 'Centrální sklad',
            #     'note': 'Stainless steel, strong bond.',
            #     'supplier_set': [
            #         {"supplier": 1, "manufacturer": 2}
            #     ]
            # },
            # {
            #     'name': 'Dental Tray Paper',
            #     'quantity': 2000,
            #     'min_quantity': 200,
            #     'expiration_date': '2025-06-15',
            #     'product_type': 'Materiál',
            #     'stock_number': 'Lokace 1',
            #     'note': 'Absorbent, single-use.',
            #     'supplier_set': [
            #         {"supplier": 3, "manufacturer": 4}
            #     ]
            # },
            # {
            #     'name': 'Disposable Syringe',
            #     'quantity': 1000,
            #     'min_quantity': 100,
            #     'expiration_date': '2026-01-01',
            #     'product_type': 'Materiál',
            #     'stock_number': 'Centrální sklad',
            #     'note': 'Sterile, single-use.',
            #     'supplier_set': [
            #         {"supplier": 5, "manufacturer": 6}
            #     ]
            # },
            # {
            #     'name': 'Dental X-ray Sensor',
            #     'quantity': 15,
            #     'min_quantity': 2,
            #     'expiration_date': '2031-04-04',
            #     'product_type': 'Zařízení',
            #     'stock_number': 'Lokace 2',
            #     'note': 'High-resolution imaging.',
            #     'supplier_set': [
            #         {"supplier": 7, "manufacturer": 8}
            #     ]
            # },
            # {
            #     'name': 'Dental Articulator',
            #     'quantity': 35,
            #     'min_quantity': 3,
            #     'expiration_date': '2030-12-12',
            #     'product_type': 'Zařízení',
            #     'stock_number': 'Centrální sklad',
            #     'note': 'Adjustable, accurate simulations.',
            #     'supplier_set': [
            #         {"supplier": 9, "manufacturer": 10}
            #     ]
            # },
            # {
            #     'name': 'Dental Spatula',
            #     'quantity': 60,
            #     'min_quantity': 6,
            #     'expiration_date': '2027-05-05',
            #     'product_type': 'Nástroj',
            #     'stock_number': 'Lokace 2',
            #     'note': 'Stainless steel, non-stick surface.',
            #     'supplier_set': [
            #         {"supplier": 11, "manufacturer": 12}
            #     ]
            # }
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

                # Extract supplier_set and stock from data and remove from data dictionary
                supplier_set_data = data.pop('supplier_set', [])
                stock_data = data.pop('stock', [])

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

                # Create Stock instances
                for stock_data_item in stock_data:
                    store_id = stock_data_item.get('store')
                    quantity = stock_data_item.get('quantity')

                    store = Store.objects.get(pk=store_id)

                    Stock.objects.create(product=product, store=store, quantity=quantity)

        self.stdout.write(self.style.SUCCESS('Products imported successfully.'))

