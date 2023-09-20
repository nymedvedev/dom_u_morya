# ФАЙЛ ДЛЯ СОЗДАНИЯ АДМИНКИ ДЛЯ ОБРАБОТКИ ЗАКАЗОВ
from django.contrib import admin

# 1) импортирую модель
from orders.models import Order

# 3) дабавил декоратор:
@admin.register(Order)
# 2) создаю класс:
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "house", "date"]
