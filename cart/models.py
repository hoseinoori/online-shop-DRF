from django.db import models

from product.models import Product
from user.models import User


# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Order(models.Model):
    oStatus = [
        ("pending", "pending"),
        ("paid", "paid"),
        ("processing", "processing"),
        ("shipped", "shipped"),
        ("delivered", "delivered"),
        ("cancelled", "cancelled"),
        ("returned", "returned")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    shipping_cost = models.IntegerField(default=0)
    discount_percent = models.IntegerField(default=0)
    final_price = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=oStatus, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.final_price = self.total_price - self.total_price * self.discount_percent / 100 + self.shipping_cost

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user.username} - {self.status}"


class OrderItem(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    subtotal = models.IntegerField()

    def save(self, *args, **kwargs):
        self.subtotal = self.product.price * self.quantity

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Payment(models.Model):
    pStatus = [
        ("pending", "pending"),
        ("success", "success"),
        ("failed", "failed"),
        ("refunded", "refunded"),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    authority = models.TextField(blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    gateway = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=pStatus, default='pending')
    paid_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.user.username} - {self.status}"
