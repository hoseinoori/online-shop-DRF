from django.contrib import admin

from .models import Cart, CartItem, Order, OrderItem, Payment


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'price', 'created_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price', 'status', 'created_at']
    list_editable = ['status']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'subtotal']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'amount', 'gateway', 'status', 'created_at', 'paid_at']
    list_editable = ['status']


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)
