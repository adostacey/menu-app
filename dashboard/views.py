from typing import Any
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from menus import models


# Create your views here.
class RestaurantListView(LoginRequiredMixin, ListView):
    model = models.Restaurant
    context_object_name = "restaurants"
    template_name = "dashboard/restaurant_list.html"


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    context_object_name = "categories"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        queryset = models.Category.objects.filter(restaurant__slug=slug)
        return queryset
    

    template_name = "dashboard/categories_list.html"


class ItemListView(LoginRequiredMixin, ListView):
    model = models.Item
    template_name = "dashboard/items_list.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["category"] = models.Category.objects.get(pk=pk)
        return context


class CreateItemView(LoginRequiredMixin, CreateView):
    model = models.Item
    fields = "__all__"
    template_name = "dashboard/create_item.html"

    def get_initial(self):
        initial = super().get_initial()
        category_pk = self.kwargs.get("pk")
        try:
            category = models.Category.objects.get(pk=category_pk)
            initial["Category"] = category
            initial["restaurant"] = category.restaurant
        except models.Category.DoesNotExist:
            raise Http404("Category does not exist")
        return initial

    def get_success_url(self) -> str:
        url = reverse(
            "items-list",
            kwargs={"slug": self.object.Category.restaurant.slug, "pk": self.kwargs.get("pk")},
        )
        return url
