'''Admin panel for products and categories'''
from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    '''Admin panel for products'''
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "has_size",
        "rating",
        "image",
        "stock",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    '''Admin panel for categories'''
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
