from django.core.management.base import BaseCommand
from django.db import connection

from accounts.models import CustomUser
from core.models import Supplier, Table


class Command(BaseCommand):
    help = 'Import tables into the database'

    def handle(self, *args, **kwargs):
        table_data = [
            {
                'title': 'Centrální sklad',
            },
            {
                'title': 'Lokace 1',
            },
            {
                'title': 'Lokace 2',
            },
        ]

        # Delete all rows from the Supplier table
        Table.objects.all().delete()

        # Reset autoincrement to start with id 1
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='core_table';")

        for data in table_data:
            table = Table(**data)
            table.save()

        self.stdout.write(self.style.SUCCESS('Tables imported successfully.'))

