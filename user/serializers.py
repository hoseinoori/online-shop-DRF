from rest_framework import serializers

from user.models import User, Avatar, Address


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'first_name', 'last_name', 'password', 'avatar', 'address')
