from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Category, Item, Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "slug"]


@admin.register(Category)
class CategoryAmdin(admin.ModelAdmin):
    list_filter = ["restaurant"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "restaurant", "Category"]
    list_filter = ["restaurant", "Category"]
