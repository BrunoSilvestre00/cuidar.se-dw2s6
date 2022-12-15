from django.contrib import admin
from status.models import Anotation


@admin.register(Anotation)
class AnotationAdmin(admin.ModelAdmin):
    pass