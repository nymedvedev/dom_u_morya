# ФАЙЛ С ЛОГИКОЙ РАБОТЫ ПРИЛОЖЕНИЯ

from django.shortcuts import render
# импортируем модель, т.к. дома (которые будем отображать на сайте,
# хранятся в БД, а доступ к БД через модели)
from houses.models import House


# Ф-ЦИЯ (называется "представление") ГЕНЕРИРУЕТ HTML-стр. И ВОЗВРАЩАЕТ ЕЁ ЮЗЕРУ:
def houses_list(request):
    houses = House.objects.all()
    # выведем инфо о домах в консоль:
    for house in houses:
        print(house.name, house.price)
    # свяжем представление (houses_list) c шаблоном (houses_list.html)
    return render(request, "houses/houses_list.html", {"houses": houses})
# Ф-ЦИЯ houses_list ВОЗВРАЩАЕТ РЕЗУЛЬТАТ ФУНКЦИИ render,
# КОТОРАЯ ПРИНИМАЕТ:
# 1) ЗАПРОС (request) ЮЗЕРА,
# 2) НАЗВ. ШАБЛОНА ("houses/houses_list.html")
# 3) словарь для вывода данных в html (на сайт)
