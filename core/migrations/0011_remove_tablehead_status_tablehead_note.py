# Generated by Django 5.0.3 on 2024-04-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_order_no_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablehead',
            name='status',
        ),
        migrations.AddField(
            model_name='tablehead',
            name='note',
            field=models.CharField(default='Poznámka', max_length=100),
        ),
    ]