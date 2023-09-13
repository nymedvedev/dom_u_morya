from django.db import models

class House(models.Model):
    name = models.CharField("название", max_length=50)
    price = models.IntegerField("цена")
    description = models.TextField("описание")
