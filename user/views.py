from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from user.models import User, Address, Avatar
from user.serializers import UserSerializer, AddressSerializer, AvatarSerializer


# Create your views here.

@extend_schema(tags=["Users"])
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@extend_schema(tags=["User Avatars"])
class AvatarViewSet(viewsets.ModelViewSet):
    serializer_class = AvatarSerializer
    queryset = Avatar.objects.all()


@extend_schema(tags=["User Addresses"])
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
