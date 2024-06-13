from django.urls import path
from . import views

urlpatterns = [path("johns/", views.MenuView.as_view(), name="menu-johns")]
