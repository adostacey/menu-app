from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    hours_of_operation = models.CharField(max_length=200)
    facebook = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name} ({self.restaurant.name[:4]})"


class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    price_1 = models.FloatField()
    price_1_descr = models.CharField(max_length=50, blank=True)
    price_2 = models.FloatField(null=True, blank=True)
    price_2_descr = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name
