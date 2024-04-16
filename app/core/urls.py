from django.urls import include, path
from rest_framework import routers

from core.views import TableViewSet, TableHeadViewSet, ProductViewSet, ProductUpdateAPIView, ProductChoicesViewSet

router = routers.DefaultRouter()
router.register('tables', TableViewSet)
router.register('table-heads', TableHeadViewSet)
router.register('products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product-choices/', ProductChoicesViewSet.as_view({'get': 'list'}), name='product-choices'),
]