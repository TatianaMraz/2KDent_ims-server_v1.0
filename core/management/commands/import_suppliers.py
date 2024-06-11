from django.core.management.base import BaseCommand
from django.db import connection

from accounts.models import CustomUser
from core.models import Supplier


class Command(BaseCommand):
    help = 'Import suppliers into the database'

    def handle(self, *args, **kwargs):
        default_user = CustomUser.objects.get(username='npgroup-admin')

        supplier_data = [
            {
                'company': 'MedTech Europe',
                'address': '123 Avenue Street, Paris, France',
                'ico': 'FR1234567890',
                'bank_account': 'FR76 1234 5678 9012 3456 7890 123',
            },
            {
                'company': 'EuroMed Supplies',
                'address': '456 Plaza Road, Madrid, Spain',
                'ico': 'ES0987654321',
                'bank_account': 'ES98 7654 3210 9876 5432 1098 765',
                'note': 'Specializes in surgical instruments and devices.',
            },
            {
                'company': 'Medico Europe Ltd',
                'address': '123 Medical Street',
                'ico': 'EU123456789',
                'bank_account': 'DE12345678901234567890',
            },
            {
                'company': 'Alpha Health Supplies',
                'address': '456 Health Avenue',
                'ico': 'EU987654321',
                'bank_account': 'DE23456789012345678901',
            },
            {
                'company': 'Euro MedTech',
                'address': '789 Tech Boulevard',
                'ico': 'EU246813579',
                'bank_account': 'IT34567890123456789012',
            },
            {
                'company': 'Vitalis Medical',
                'address': '202 Vitality Lane',
                'ico': 'EU654789321',
                'bank_account': 'NL45678901234567890123',
            },
            {
                'company': 'Biomed Solutions',
                'address': '303 BioTech Street',
                'ico': 'EU147258369',
                'bank_account': 'PL56789012345678901234',
            },
            {
                'company': 'MediCare Europe',
                'address': '404 Care Avenue',
                'ico': 'EU753159264',
                'bank_account': 'BE67890123456789012345',
            },
            {
                'company': 'Omega Medical',
                'address': '505 Omega Drive',
                'ico': 'EU582471396',
                'bank_account': 'PT78901234567890123456',
            },
            {
                'company': 'HealthFirst Europe',
                'address': '606 Health Road',
                'ico': 'EU369852147',
                'bank_account': 'CZ89012345678901234567',
            },
            {
                'company': 'MediTech Solutions',
                'address': '707 Tech Street',
                'ico': 'EU951357486',
                'bank_account': 'SE90123456789012345678',
            },
            {
                'company': 'Zenith Healthcare',
                'address': '909 Zenith Square',
                'ico': 'EU123789456',
                'bank_account': 'AT01234567890123456789',
            },
            {
                'company': 'EuroMed Industries',
                'address': '444 EuroMed Street',
                'ico': 'EU147852369',
                'bank_account': 'DK34567890123456789012',
            },
            {
                'company': 'HealthTech Europe',
                'address': '555 HealthTech Road',
                'ico': 'EU369874125',
                'bank_account': 'FI45678901234567890123',
            },
            {
                'company': 'Medica Solutions',
                'address': '333 Medica Plaza',
                'ico': 'EU654123987',
                'bank_account': 'HU56789012345678901234',
            },
            {
                'company': 'MedWorld Solutions',
                'address': '777 World Plaza',
                'ico': 'EU582963741',
                'bank_account': 'SK67890123456789012345',
            },
        ]

        # Delete all rows from the Supplier table
        Supplier.objects.all().delete()

        # Reset autoincrement to start with id 1
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='core_supplier';")

        for data in supplier_data:
            data['created_by'] = default_user
            supplier = Supplier(**data)
            supplier.save()

        self.stdout.write(self.style.SUCCESS('Suppliers imported successfully.'))

