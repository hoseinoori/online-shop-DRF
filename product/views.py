from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from product.models import Product, Coupon, Category, ProductImage, Review, WishList
from product.serializers import ProductSerializer, CouponSerializer, CategorySerializer, ProductImageSerializer, \
    ReviewSerializer, WishListSerializer


# Create your views here.
@extend_schema(tags=["Products"])
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)


@extend_schema(tags=["Categories"])
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)


@extend_schema(tags=["Product Images"])
class ProductImageViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.filter(is_active=True)


@extend_schema(tags=["Coupon Codes"])
class CouponViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.filter(is_active=True)


@extend_schema(tags=["Reviews"])
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.filter(is_approved=True)


@extend_schema(tags=["WishLists"])

class WishListViewSet(viewsets.ModelViewSet):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()
