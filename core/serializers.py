
from rest_framework import serializers

from .models import Table, TableHead, Product, Order, Supplier, Manufacturer, SupplierSet


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class TableHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableHead
        fields = '__all__'


class SupplierSetSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())

    class Meta:
        model = SupplierSet
        fields = ['supplier', 'manufacturer']


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    updated_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    supplier_set = SupplierSetSerializer(many=True)

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

    def create(self, validated_data):
        supplier_set_data = validated_data.pop('supplier_set', [])
        product = Product.objects.create(**validated_data)

        for item in supplier_set_data:
            SupplierSet.objects.create(product=product, **item)

        return product

    def update(self, instance, validated_data):
        supplier_set_data = validated_data.pop('supplier_set', [])
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.min_quantity = validated_data.get('min_quantity', instance.min_quantity)
        instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)
        instance.product_type = validated_data.get('product_type', instance.product_type)
        instance.stock_number = validated_data.get('stock_number', instance.stock_number)
        instance.image = validated_data.get('image', instance.image)
        instance.note = validated_data.get('note', instance.note)
        instance.save()

        # Update supplier sets
        instance.supplier_set.all().delete()
        for item in supplier_set_data:
            SupplierSet.objects.create(product=instance, **item)

        return instance


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
