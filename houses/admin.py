# ПАНЕЛЬ АДМИНИСТРИРОВАНИЯ ПРИЛОЖЕНИЯ.
# добавим в неё наше прилож. по упр. домами

from django.contrib import admin # строка django по-ум.
# свяжем класс HouseAdmin с моделью House:
# для этого 1) импортируем House из моделей проги
from houses.models import House
# 2) используем декоратор:
@admin.register(House)

class HouseAdmin(admin.ModelAdmin):
# родительский класс ModelAdmin отв. за формирование админки для моделей.
# унаследованный класс HouseAdmin отв. за админку модели House

    # добавим в инфо о доме цену:
    list_display = ["name", "price"]