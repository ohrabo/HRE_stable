from .models import Category, Marker
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Marker)
class MarkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'lat', 'lon', 'category']
    list_filter = ['name', 'category']
    search_fields = ['name', 'date', 'category']
    prepopulated_fields = {'slug': ('name',)}

