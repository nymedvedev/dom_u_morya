# ФАЙЛ С ЛОГИКОЙ РАБОТЫ ПРИЛОЖЕНИЯ

from django.shortcuts import render
# Ф-ЦИЯ (называется "представление") ГЕНЕРИРУЕТ HTML-стр. И ВОЗВРАЩАЕТ ЕЁ ЮЗЕРУ:
def houses_list(request):
    # свяжем представление (houses_list) c шаблоном (houses_list.html)
    return render(request, "houses/houses_list.html")
# Ф-ЦИЯ houses_list ВОЗВРАЩАЕТ РЕЗУЛЬТАТ ФУНКЦИИ render,
# КОТОРАЯ ПРИНИМАЕТ: 1) ЗАПРОС (request) ЮЗЕРА, 2) НАЗВ. ШАБЛОНА ("houses/houses_list.html")
