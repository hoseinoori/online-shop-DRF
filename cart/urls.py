from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.views import CartViewSet, CartItemViewSet, OrderViewSet, OrderItemViewSet, PaymentViewSet

router = DefaultRouter()
router.register('', CartViewSet)
router.register('items', CartItemViewSet)
router.register('orders', OrderViewSet)
router.register('orders/items', OrderItemViewSet)
router.register('payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
