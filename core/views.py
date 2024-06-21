from django.db.models import ProtectedError
from django.http import JsonResponse
from knox.auth import TokenAuthentication
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.forms import ProductForm
from core.models import Table, TableHead, Product, Order, Supplier, Manufacturer
from core.serializers import TableSerializer, TableHeadSerializer, ProductSerializer, OrderSerializer, \
    SupplierSerializer, ManufacturerSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableHeadViewSet(viewsets.ModelViewSet):
    queryset = TableHead.objects.all()
    serializer_class = TableHeadSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ProductChoicesViewSet(viewsets.ViewSet):
    def list(self, request):
        product_type_choices = dict(Product.PRODUCT_TYPE_CHOICES)
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


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response({
                'error': "Supplier can't be deleted because it is referenced by existing products.",
                'code': 'protected_error'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Supplier.DoesNotExist:
            return Response({
                'error': 'Supplier not found',
                'code': 'not_found'
            }, status=status.HTTP_404_NOT_FOUND)


class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ManufacturerUpdateAPIView(generics.UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
