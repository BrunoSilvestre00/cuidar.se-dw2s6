from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as SuperUserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(SuperUserAdmin):
    pass
