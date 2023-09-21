# ФАЙЛ С ЛОГИКОЙ РАБОТЫ ПРИЛОЖЕНИЯ

# импортируем render, которая создаёт отв. на запросы в виде html
# импортируем get_object_or_404, чтобы получить объект или 404, если объект был удалён
from django.shortcuts import render, get_object_or_404

# импортируем функцию перенаправления, функицию генерации URL-адресов
from django.http import HttpResponseRedirect
from django.urls import reverse

# импортируем модель, т.к. дома (которые будем отображать на сайте,
# хранятся в БД, а доступ к БД через модели).
from houses.models import House
# для вывода формы на сайт создаю представление:
from orders.forms import OrderForm
#импортирую класс для фильтрации домов на стр.:
from houses.forms import HousesFilterForm

# Ф-ЦИЯ (называется "представление") ГЕНЕРИРУЕТ HTML-стр. И ВОЗВРАЩАЕТ ЕЁ ЮЗЕРУ:
def houses_list(request):
    houses = House.objects.filter(active=True)
    # получаем список активн.домов из БД ч/з модель House
    form = HousesFilterForm(request.GET) # форма фильтрации из forms.py
    if form.is_valid(): # метод проверяет, верные ли переданы данные
        if form.cleaned_data["min_price"]: # есть ли мин.цена
            houses = houses.filter(price__gte=form.cleaned_data["min_price"])
            # __gte - оставляет дома, цена к-ых больше или равна значению (greater than or equal)
        if form.cleaned_data["max_price"]:  # есть ли макс.цена
            houses = houses.filter(price__lte=form.cleaned_data["max_price"])
            # __lte - less than or equal (меньше или равно)
    # выведем инфо о домах в консоль:
    for house in houses:
        print(house.name, house.price)
    # свяжем представление (houses_list) c шаблоном (houses_list.html)
    return render(request, "houses/houses_list.html", {"houses": houses, "form": form})
    # Ф-ЦИЯ houses_list ВОЗВРАЩАЕТ РЕЗУЛЬТАТ ФУНКЦИИ render,
    # которая принимает:
    # 1) запрос (request) юзера,
    # 2) назв.шаблона ("houses/houses_list.html")
    # 3) словарь для вывода данных в html (на сайт)

# добавим представление для отобр. отд. стр. с домами:
def house_detail(request, house_id):
    # присваиваем переменной house рез-тат раб.функ. get_object_or_404,
    # кот-ая приним. модель House и пар-тр id, по кот-му б/т поиск
    # нужн. объекта. Если найден - функ.верн. его в перем. House, нет - 404:
    house = get_object_or_404(House, id=house_id, active=True)
    # добавлю форму:
    form = OrderForm(request.POST or None, initial={"house": house})
    # (request.POST or None) - передаём данные пост-запроса или None (ес.данных нет)
    # initial={"house": house} - в поле "Дом:" б/т по-умол.стоять уже выбр.тип дома
    # форма OrderForm т/рь связ. с моделью Order, к-рая св. с табл. в БД

    # проверка валидности данных юзера:
    if request.method == "POST":
        # обрабатываем данные пост-запроса
        if form.is_valid():
            # сохраняем форму:
            form.save()
            url = reverse("house", kwargs={"house_id": house.id})
            # reverse принимает 1)имя пути; 2)параметр формир-я адреса
            return HttpResponseRedirect(f"{url}?sent=1")
            # HttpResponseRedirect отв. за статус перенаправления (302 "перемещено временно")
            # ?sent=1 - параметр, к-ый добавл. в URL

    # подключу к представлению шаблон:
    return render(request, "houses/house_detail.html", {
        "house": house,
        "form": form,
        "sent": request.GET.get("sent")
        # работаем с гет-параметрами (к-ые передаются в адресной строке бр-ра)
    })
