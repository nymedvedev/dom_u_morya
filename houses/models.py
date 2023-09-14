# ФАЙЛ ДЛЯ ХРАНЕНИЯ МОДЕЛЕЙ

from django.db import models


class House(models.Model):
# класс связан через наследование - классом Model
    # атрибуты класса для хранения данных:
    name = models.CharField("название", max_length=50)
    # max_length - длина строки
    # CharField - символьные данные
    price = models.IntegerField("цена")
    # IntegerField - целые числа
    description = models.TextField("описание")

    # создаю подкласс, отв. за описательную инфо:
    class Meta:
        verbose_name = "дом" # для объектов в ед. ч.
        verbose_name_plural = "дома" # для объектов во мн. ч.
        ordering = ["name"] # добавил сортировку по алфовиту

    # метод, чтобы объекты (дома) дома в админке
    # вместо "House object" наз. наименованиями (name).
    def __str__(self):
        return self.name.upper()
        # при созд. объектов - наим. будут в верх. рег.