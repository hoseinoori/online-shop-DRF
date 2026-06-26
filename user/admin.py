from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import User, Avatar, Address


class UserAdmin(ModelAdmin):
    list_display = ['get_full_name', 'username', 'phone', 'email', 'is_staff', 'is_active']
    list_editable = ['is_active']
    search_fields = ['username', 'email', 'phone', 'first_name', 'last_name']

class AvatarAdmin(ModelAdmin):
    list_display = ['title']

class AddressAdmin(ModelAdmin):
    list_display = ['receiver_name', 'postal_code', 'city', 'is_default']
    list_editable = ['is_default']



admin.site.register(User, UserAdmin)
admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Address, AddressAdmin)
