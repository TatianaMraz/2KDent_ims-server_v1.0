from django.core.management.base import BaseCommand

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
                'company': 'MediCo GmbH',
                'address': '789 Markt Platz, Berlin, Germany',
                'ico': 'DE1122334455',
                'bank_account': 'DE65 6789 0123 4567 8901 23',
                'note': 'Reliable source for high-quality medical consumables.',
            },
            {
                'company': 'MedSupply Ltd',
                'address': '321 Square Lane, London, UK',
                'ico': 'UK9876543210',
                'bank_account': 'UK87 6543 2109 8765 4321 09',
            },
            {
                'company': 'Meditech Scandinavia',
                'address': '987 Nordic Avenue, Stockholm, Sweden',
                'ico': 'SE1122334455',
                'bank_account': 'SE12 3456 7890 1234 5678 9012',
                'note': 'Provider of innovative medical devices for Nordic region.',
            },
            {
                'company': 'MedSolutions SA',
                'address': '234 Rue de Sante, Brussels, Belgium',
                'ico': 'BE9876543210',
                'bank_account': 'BE98 7654 3210 9876 5432 1098 765',
                'note': 'Trusted supplier of medical equipment in Benelux.',
            },
            {
                'company': 'MediServe Srl',
                'address': '567 Piazza Medica, Rome, Italy',
                'ico': 'IT1234567890',
                'bank_account': 'IT34 5678 9012 3456 7890 1234 56',
            },
            {
                'company': 'MedCare ApS',
                'address': '890 Health Street, Copenhagen, Denmark',
                'ico': 'DK11223344',
                'bank_account': 'DK12 3456 7890 1234 5678 9012',
                'note': 'Specializes in medical supplies for Danish hospitals.',
            },
            {
                'company': 'MedTech Solutions',
                'address': '432 Boulevard Medico, Lisbon, Portugal',
                'ico': 'PT0987654321',
                'bank_account': 'PT98 7654 3210 9876',
            },
            {
                'company': 'Zenith Healthcare',
                'address': '909 Zenith Square',
                'ico': 'EU123789456',
                'bank_account': 'AT01234567890123456789',
                'note': 'Offers premium quality medical supplies.',
            },
            {
                'company': 'EuroMed Industries',
                'address': '444 EuroMed Street',
                'ico': 'EU147852369',
                'bank_account': 'DK34567890123456789012',
                'note': 'Provider of medical devices and instruments.',
            },
            {
                'company': 'HealthTech Europe',
                'address': '555 HealthTech Road',
                'ico': 'EU369874125',
                'bank_account': 'FI45678901234567890123',
                'note': 'Offers cutting-edge medical technology.',
            },
            {
                'company': 'Medica Solutions',
                'address': '333 Medica Plaza',
                'ico': 'EU654123987',
                'bank_account': 'HU56789012345678901234',
                'note': 'Specializes in hospital equipment.',
            },
            {
                'company': 'MedWorld Solutions',
                'address': '777 World Plaza',
                'ico': 'EU582963741',
                'bank_account': 'SK67890123456789012345',
                'note': 'Global provider of medical equipment.',
            },
        ]

        for data in supplier_data:
            data['created_by'] = default_user
            supplier = Supplier(**data)
            supplier.save()

        self.stdout.write(self.style.SUCCESS('Suppliers imported successfully.'))
