from rest_framework import serializers

from .models import Table, TableHead, Product


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class TableHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableHead
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'expiration_date': {
                'error_messages': {
                    'invalid': 'Zvolte datum ve formátu DD.MM.RRRR.'
                }
            }
        }


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'delivery_date': {
                'error_messages': {
                    'invalid': 'Zvolte datum ve formátu DD.MM.RRRR.'
                }
            }
        }