import uuid

from django.db import models

from user.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.TextField(blank=True, null=True)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.TextField()
    is_active = models.BooleanField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.TextField(blank=True, null=True)
    description = models.TextField()
    price = models.IntegerField()
    discount_percent = models.IntegerField(default=0)
    stock_quantity = models.IntegerField(verbose_name='stock')
    sku = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=300)
    images = models.ManyToManyField('ProductImage', blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_sku(self):
        pName = self.name.replace(' ', '')
        pBrand = self.brand.replace(' ', '')
        return f"product-{pName}-{pBrand}-{uuid.uuid4()}"

    def save(self, *args, **kwargs):
        if self.sku is None:
            self.sku = self.generate_sku()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.TextField()
    is_active = models.BooleanField()

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.title


class Review(models.Model):
    ratings = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(choices=ratings)
    comment = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount_percent = models.IntegerField(default=0)
    usage_limit = models.IntegerField(default=10)
    used_count = models.IntegerField(default=0)
    end_date = models.DateTimeField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def __str__(self):
        return self.code


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "WishList"
        verbose_name_plural = "WishLists"

    def __str__(self):
        return self.user.username
