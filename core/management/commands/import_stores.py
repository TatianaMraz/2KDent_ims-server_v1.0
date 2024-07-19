from django.core.management.base import BaseCommand
from core.models import Store


class Command(BaseCommand):
    help = 'Create initial store locations'

    def handle(self, *args, **kwargs):
        stores = [
            'Centrální sklad',
            'Lokace 1',
            'Lokace 2'
        ]

        for store_name in stores:
            store, created = Store.objects.get_or_create(name=store_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created store: {store_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Store already exists: {store_name}'))


