from django.db import models

# Create your models here.
class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.body[:25]