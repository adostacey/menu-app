from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Item, Restaurant


class MenuView(ListView):
    model = Category
    template_name = "menu.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["restaurant"] = "John's Waffle & Pancake House"
        return context
    