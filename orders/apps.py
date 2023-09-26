from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    # сделаю в админке "заявка\-ки" вместо "order\-s":
    verbose_name = 'заявки'
