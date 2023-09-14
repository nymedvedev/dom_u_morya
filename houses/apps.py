# НАСТРОЙКИ ПРИЛОЖЕНИЯ

from django.apps import AppConfig

class HousesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'houses'
    # менчем назв. "Houses" в админке на "Дома"
    verbose_name = "Дома"
