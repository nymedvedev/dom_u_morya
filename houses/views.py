# ФАЙЛ С ЛОГИКОЙ РАБОТЫ ПРИЛОЖЕНИЯ

from django.shortcuts import render, get_object_or_404
#импортируем get_object_or_404, чтобы

# импортируем модель, т.к. дома (которые будем отображать на сайте,
# хранятся в БД, а доступ к БД через модели).
from houses.models import House
# для вывода формы на сайт создаю представление:
from orders.forms import OrderForm

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

# добавим представление для отобр. отд. стр. с домами:
def house_detail(request, house_id):
    # присваиваем переменной house рез-тат раб.функ. get_object_or_404,
    # кот-ая приним. модель House и пар-тр id, по кот-му б/т поиск
    # нужн. объекта. Если найден - функ.верн. его в перем. House, нет - 404:
    house = get_object_or_404(House, id=house_id)
    # добавлю форму:
    form = OrderForm(request.POST or None, initial={"house": house})
    # (request.POST or None) - передаём данные пост-запроса или None (ес.данных нет)
    # initial={"house": house} - в поле "Дом:" б/т по-умол.стоять уже выбр.тип дома

    # проверка валидности данных юзера:
    if request.method == "POST":
        if form.is_valid():
            # сохраняем форму:
            form.save()
    # форма OrderForm т/рь связ. с моделью Order, к-рая св. с табл. в БД
    # подключу к представлению шаблон:
    return render(request, "houses/house_detail.html", {"house": house, "form": form})

