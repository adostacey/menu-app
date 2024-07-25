from typing import Any
from django.views.generic import ListView
from posts.models import Post
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

    queryset = Post.objects.all().order_by("-date_created")[:3]