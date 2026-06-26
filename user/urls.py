from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user.views import UserViewSet, AddressViewSet, AvatarViewSet

router = DefaultRouter()
router.register('', UserViewSet)
router.register('address', AddressViewSet)
router.register('avatar', AvatarViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
