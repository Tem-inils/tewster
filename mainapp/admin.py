from django.contrib import admin
from .models import ProductImage, MainProduct


# Register your models here.
@admin.register(MainProduct)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title']
    list_display = ['id', 'title', 'category']
    list_filter = ['id']


@admin.register(ProductImage)
class ProductImageManyToMany(admin.ModelAdmin):
    search_fields = ['id', 'product']
    list_display = ['id', 'product', 'img']
    list_filter = ['id']
