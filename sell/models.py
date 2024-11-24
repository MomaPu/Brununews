from django.db import models

class Category(models.Model):

    name = models.CharField("Наименование",max_length=100, unique=True)

from django.db import models

class Product(models.Model):

    name = models.CharField("Название",max_length=64, unique=True)
    price = models.DecimalField("Стоимость", max_digits=12, decimal_places=2)
    text = models.TextField("Текст новости")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)