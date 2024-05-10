from rest_framework import serializers

from .models import Table, TableHead, Product, Order, OrderItem


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
        model = Order
        fields = ('id', 'order_number', 'supplier', 'created_at', 'updated_at', 'order_date', 'delivery_date', 'is_delivered', 'items')
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


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
