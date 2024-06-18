from django.urls import path
from . import views

urlpatterns = [path("<slug:slug>/", views.MenuView.as_view(), name="menu")]
