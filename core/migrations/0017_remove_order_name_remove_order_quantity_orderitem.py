# Generated by Django 5.0.3 on 2024-04-29 12:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_tablehead_is_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
    ]
