from django.contrib import admin

from core.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

