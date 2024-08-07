from django.http import JsonResponse
from rest_framework import viewsets, generics

from core.forms import ProductForm
from core.models import Table, TableHead, Product
from core.serializers import TableSerializer, TableHeadSerializer, ProductSerializer


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
        status_choices = dict(Product.status_choices)
        product_type_choices = dict(Product.product_type_choices)
        choices = {
            'status_choices': status_choices,
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