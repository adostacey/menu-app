from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("pages.urls")),
    path("menu/", include("menus.urls")),
    path("admin/", admin.site.urls),
]
