from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, CategoryViewSet, ProductImageViewSet, ReviewViewSet, WishListViewSet, \
    CouponViewSet

router = DefaultRouter()
router.register('', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('images', ProductImageViewSet)
router.register('wishlists', WishListViewSet)
router.register('coupons', CouponViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
