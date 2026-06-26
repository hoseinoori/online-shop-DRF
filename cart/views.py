from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from cart.models import Cart, CartItem, Order, OrderItem, Payment
from cart.serializers import CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer, PaymentSerializer


# Create your views here.
@extend_schema(tags=["Carts"])
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


@extend_schema(tags=["Cart Items"])
class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


@extend_schema(tags=["Orders"])
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


@extend_schema(tags=["Order Items"])
class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


@extend_schema(tags=["Payments"])
class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
