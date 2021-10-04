from django.contrib import admin

# Register your models here.

from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "image", "status")
    search_fields = ("title",)