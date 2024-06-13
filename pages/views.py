from django.views.generic import ListView
from menus.models import Restaurant
# Create your views here.

class HomeView(ListView):
    model = Restaurant
    template_name = "home.html"
    context_object_name = "restaurants"