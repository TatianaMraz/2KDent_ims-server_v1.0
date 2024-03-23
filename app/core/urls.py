from django.urls import include, path
from rest_framework import routers

from core.views import TableViewSet

router = routers.DefaultRouter()
router.register('tables', TableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]