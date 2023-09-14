# ФАЙЛ С ЛОГИКОЙ РАБОТЫ ПРИЛОЖЕНИЯ

from django.shortcuts import render
# Ф-ЦИЯ ГЕНЕРИРУЕТ HTML-стр. И ВОЗВРАЩАЕТ ЕЁ ЮЗЕРУ:
def houses_list(request):
    return render(request, "houses/houses_list.html")
# Ф-ЦИЯ houses_list ВОЗВРАЩАЕТ ЗАПРОС (request) ФУНКЦИИ render,
# КОТОРАЯ ПРИНИМАЕТ: 1) ЗАПРОС (request) ЮЗЕРА, 2) НАЗВ. ШАБЛОНА ("houses/houses_list.html")
