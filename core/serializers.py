from rest_framework import serializers

from .models import Table, TableHead, Product, Order, Supplier, Manufacturer


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class TableHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableHead
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    updated_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

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
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'order_date': {
                'error_messages': {
                    'invalid': 'Zvolte datum ve formátu DD.MM.RRRR.'
                }
            },
            'delivery_date': {
                'error_messages': {
                    'invalid': 'Zvolte datum ve formátu DD.MM.RRRR.'
                }
            }
        }


class SupplierSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    updated_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Supplier
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    updated_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Manufacturer
        fields = '__all__'
