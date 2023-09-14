from django.contrib import admin
from houses.models import House
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]