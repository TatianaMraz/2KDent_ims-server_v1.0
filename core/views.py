from django.http import JsonResponse
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action

from core.forms import ProductForm
from core.models import Table, TableHead, Product, Order, OrderItem
from core.serializers import TableSerializer, TableHeadSerializer, ProductSerializer, OrderSerializer, \
    OrderItemSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableHeadViewSet(viewsets.ModelViewSet):
    queryset = TableHead.objects.all()
    serializer_class = TableHeadSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductChoicesViewSet(viewsets.ViewSet):
    def list(self, request):
        product_type_choices = dict(Product.product_type_choices)
        choices = {
            'product_type_choices': product_type_choices
        }
        return JsonResponse(choices)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def product_image_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Successfully uploaded'}, status=201)
        else:
            form = ProductForm()
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'message': 'Method not allowed'}, status=405)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['POST'])
    def add_item(self, request, pk=None):
        if 'name' in request.data and 'quantity' in request.data:
            order = self.get_object()
            name = request.data['name']
            quantity = request.data['quantity']

            item, created = OrderItem.objects.update_or_create(order=order, name=name, quantity=quantity)
            serializer = OrderItemSerializer(item)
            response = {
                'message': 'položka upravena' if not created else 'položka upravena',
                'result': serializer.data
            }
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'zadejte položku objednávky'}
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



