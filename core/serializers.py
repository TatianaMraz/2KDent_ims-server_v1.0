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


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'name', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

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

    def validate(self, data):
        if not data.get('items'):
            raise serializers.ValidationError('Je vyžadována minimálne jedna položka pro objednávku.')
        return data

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)
        for items_data in items_data:
            OrderItem.objects.create(order=order, **items_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.order_number = validated_data.get('order_number', instance.order_number)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.is_delivered = validated_data.get('is_delivered', instance.is_delivered)
        instance.save()

        # Remove items that are not in the update data
        current_item_ids = [item.id for item in instance.items.all()]
        new_item_ids = [item['id'] for item in items_data if 'id' in item]
        for item_id in current_item_ids:
            if item_id not in new_item_ids:
                OrderItem.objects.get(id=item_id).delete()

        # Update or create items
        for item_data in items_data:
            item_id = item_data.get('id')
            if item_id:
                item = OrderItem.objects.get(id=item_id, order=instance)
                item.name = item_data.get('name', item.name)
                item.quantity = item_data.get('quantity', item.quantity)
                item.save()
            else:
                OrderItem.objects.create(order=instance, **item_data)

        return instance




