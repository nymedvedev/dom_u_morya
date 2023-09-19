# ФАЙЛ ДЛЯ СОЗДАНИЯ ФОРМЫ ДЛЯ ЗАПОЛНЕНИЯ КЛИЕНТОМ НА САЙТЕ

from django import forms
# импортирую модель:
from orders.models import Order

# класс OrderForm унаследован от ModelForm,
# т.к. я хочу создать форму на осн. модели:
class OrderForm(forms.ModelForm):
    # свяжем форму и модель:
    class Meta:
        model = Order
        # укажу поля, которые отобразить:
        fields = ["house", "name", "phone"]
        # id и date не указал, это поля, которые нужны мне (не клиенту)