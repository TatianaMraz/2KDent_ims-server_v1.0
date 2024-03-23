from django.urls import include, path
from rest_framework import routers

from core.views import TableViewSet, TableHeadViewSet

router = routers.DefaultRouter()
router.register('tables', TableViewSet)
router.register('table-heads', TableHeadViewSet)


urlpatterns = [
    path('', include(router.urls)),
]