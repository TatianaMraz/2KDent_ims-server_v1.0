from django.core.management.base import BaseCommand
from django.db import connection

from accounts.models import CustomUser
from core.models import Supplier, Manufacturer


class Command(BaseCommand):
    help = 'Import manufacturers into the database'

    def handle(self, *args, **kwargs):
        default_user = CustomUser.objects.get(username='npgroup-admin')

        manufacturer_data = [
            {
                'company': 'DentalCorp Europe',
                'address': '12 Rue de Paris, Lyon, France',
                'ico': '1234567890',
                'dic': 'FR1234567890',
                'note': 'Leading supplier of dental instruments.',
            },
            {
                'company': 'SmileTech USA',
                'address': '200 Main St, New York, USA',
                'ico': '0987654321',
                'dic': 'US0987654321',
                'note': 'Innovative dental equipment manufacturer.',
            },
            {
                'company': 'OralCare GmbH',
                'address': '34 Berliner Strasse, Berlin, Germany',
                'ico': '1122334455',
                'dic': 'DE1122334455',
                'note': 'Specializes in dental hygiene products.',
            },
            {
                'company': 'DentPro Inc.',
                'address': '789 Elm St, Los Angeles, USA',
                'ico': '2233445566',
                'dic': 'US2233445566',
                'note': 'High-quality dental implants.',
            },
            {
                'company': 'EuroDental Supplies',
                'address': '56 Market Square, Brussels, Belgium',
                'ico': '3344556677',
                'dic': 'BE3344556677',
                'note': 'Wide range of dental consumables.',
            },
            {
                'company': 'Dental Solutions Ltd.',
                'address': '22 King St, London, UK',
                'ico': '4455667788',
                'dic': 'GB4455667788',
                'note': 'Comprehensive dental solutions provider.',
            },
            {
                'company': 'MediDent AG',
                'address': '78 Zurich Blvd, Zurich, Switzerland',
                'ico': '5566778899',
                'dic': 'CH5566778899',
                'note': 'Premium dental instruments and tools.',
            },
            {
                'company': 'OdontoTech Brazil',
                'address': '123 Rio St, Sao Paulo, Brazil',
                'ico': '6677889900',
                'dic': 'BR6677889900',
                'note': 'Advanced dental technology manufacturer.',
            },
            {
                'company': 'Dental Innovations LLC',
                'address': '890 Lake Shore Dr, Chicago, USA',
                'ico': '7788990011',
                'dic': 'US7788990011',
                'note': 'Pioneers in digital dental solutions.',
            },
            {
                'company': 'ScandiDent AB',
                'address': '45 Stockholm Rd, Stockholm, Sweden',
                'ico': '8899001122',
                'dic': 'SE8899001122',
                'note': 'Expert in dental prosthetics.',
            },
            {
                'company': 'LatinDent SA',
                'address': '67 Montevideo Ave, Montevideo, Uruguay',
                'ico': '9900112233',
                'dic': 'UY9900112233',
                'note': 'Dental materials for Latin America.',
            },
            {
                'company': 'Dental Masters Inc.',
                'address': '345 Industry Blvd, Toronto, Canada',
                'ico': '0011223344',
                'dic': 'CA0011223344',
                'note': 'High-performance dental drills.',
            },
            {
                'company': 'PuraDent Italia',
                'address': '56 Roma St, Rome, Italy',
                'ico': '1122334455',
                'dic': 'IT1122334455',
                'note': 'Renowned for dental adhesives.',
            },
            {
                'company': 'DentalTech Spain',
                'address': '78 Barcelona Rd, Barcelona, Spain',
                'ico': '2233445566',
                'dic': 'ES2233445566',
                'note': 'Cutting-edge dental technology.',
            },
            {
                'company': 'Nordic Dental AS',
                'address': '34 Oslo Gate, Oslo, Norway',
                'ico': '3344556677',
                'dic': 'NO3344556677',
                'note': 'Innovative dental hygiene solutions.',
            },
            {
                'company': 'Pacific Dental Co.',
                'address': '456 Bay Area Blvd, San Francisco, USA',
                'ico': '4455667788',
                'dic': 'US4455667788',
                'note': 'Leading provider of dental scalers.',
            },
            {
                'company': 'DentCare Mexico',
                'address': '789 Centro Ave, Mexico City, Mexico',
                'ico': '5566778899',
                'dic': 'MX5566778899',
                'note': 'Comprehensive dental care products.',
            },
            {
                'company': 'Dentex Poland',
                'address': '90 Warsaw St, Warsaw, Poland',
                'ico': '6677889900',
                'dic': 'PL6677889900',
                'note': 'Supplier of dental consumables.',
            },
            {
                'company': 'Dental Essentials Pty',
                'address': '12 Sydney Rd, Sydney, Australia',
                'ico': '7788990011',
                'dic': 'AU7788990011',
                'note': 'Essentials for modern dentistry.',
            },
            {
                'company': 'DentalTech Ireland',
                'address': '34 Dublin St, Dublin, Ireland',
                'ico': '8899001122',
                'dic': 'IE8899001122',
                'note': 'Advanced dental equipment.',
            },
        ]

        # Delete all rows from the Supplier table
        Manufacturer.objects.all().delete()

        # Reset autoincrement to start with id 1
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='core_manufacturer';")

        for data in manufacturer_data:
            data['created_by'] = default_user
            manufacturer = Manufacturer(**data)
            manufacturer.save()

        self.stdout.write(self.style.SUCCESS('Manufacturers imported successfully.'))

