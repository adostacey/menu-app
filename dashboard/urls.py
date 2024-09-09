from django.urls import path
from . import views

urlpatterns = [
    path("", views.RestaurantListView.as_view(), name="index-dashboard"),
    path("<slug:slug>/", views.CategoryListView.as_view(), name="category-list"),
    path("<slug:slug>/<int:pk>", views.ItemListView.as_view(), name="items-list"),
    path("<slug:slug>/<int:pk>/create", views.CreateItemView.as_view(), name="create-item")
]
