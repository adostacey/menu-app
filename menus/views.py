from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Item, Restaurant


class MenuView(ListView):
    model = Category
    template_name = "menu.html"
    context_object_name = "categories"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        rest_id = Restaurant.objects.get(slug=slug)
        return Category.objects.filter(restaurant=rest_id)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        slug = self.kwargs.get("slug")
        context = super().get_context_data(**kwargs)
        context["restaurant"] = Restaurant.objects.get(slug=slug)
        return context
