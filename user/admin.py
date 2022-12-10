import binascii
import os
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as SuperUserAdmin
from .models import ApiToken, User

# Register your models here.
@admin.register(User)
class UserAdmin(SuperUserAdmin):
    pass


@admin.register(ApiToken)
class ApiTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')

    fieldsets = (
        ('Required Information', {'fields': ('name',)}),
        ('Additional Information', {'fields': ('key_message',)}),
    )
    readonly_fields = ('key_message',)

    search_fields = ('id', 'name',)

    def has_delete_permission(self, request, obj=None):
        return False

    def key_message(self, obj):
        return obj.key

    def save_model(self, request, obj, form, change):
        if not obj.key:
            obj.key = binascii.hexlify(os.urandom(20)).decode()
            messages.add_message(request, messages.WARNING, ('The API Key for %s is %s. Please note it since you will not be able to see it again.' % (obj.name, obj.key)))
        obj.save()