from django.contrib import admin
from .models import TypeBody

@admin.register(TypeBody)
class TypeBodyAdmin(admin.ModelAdmin):
    list_display = ('type',)