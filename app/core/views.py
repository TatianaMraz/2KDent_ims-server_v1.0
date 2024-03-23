from rest_framework import viewsets

from core.models import Table
from core.serializers import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer