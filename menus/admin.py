from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Category, Item, Restaurant

# Register your models here.
admin.site.register([Category, Restaurant])


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "restaurant", "Category"]
