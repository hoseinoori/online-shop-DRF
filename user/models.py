from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Avatar(models.Model):
    title = models.CharField(max_length=100)
    image = models.TextField()

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatars"

    def __str__(self):
        return self.title


class Address(models.Model):
    receiver_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    address = models.TextField()
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.receiver_name


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
