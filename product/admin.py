from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Product, ProductImage, Category, Coupon, Review, WishList


# Register your models here.

class ProductAdmin(ModelAdmin):
    list_display = ['name', 'brand', 'category', 'price', 'stock_quantity', 'sku', 'is_active']
    list_editable = ['is_active']
    search_fields = ['name', 'brand', 'category__name']


class ProductImageAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'parent', 'is_active']
    list_editable = ['is_active']


class CouponAdmin(ModelAdmin):
    list_display = ['code', 'discount_percent', 'usage_limit', 'used_count', 'created_at', 'end_date', 'is_active']
    list_editable = ['usage_limit', 'is_active']


class ReviewAdmin(ModelAdmin):
    list_display = ['user', 'product', 'rate', 'is_approved']
    list_editable = ['is_approved']
    list_filter = ['is_approved']


class WishListAdmin(ModelAdmin):
    list_display = ['user']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(WishList, WishListAdmin)
