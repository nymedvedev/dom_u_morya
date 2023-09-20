# ФАЙЛ ДЛЯ СОЗДАНИЯ ФОРМЫ ДЛЯ ЗАПОЛНЕНИЯ КЛИЕНТОМ НА САЙТЕ

from django import forms
# импортирую модель:
from orders.models import Order

# для "скрытия" выбора дома импортируем модель:
from houses.models import House

# класс OrderForm унаследован от ModelForm,
# т.к. я хочу создать форму на осн. модели:
class OrderForm(forms.ModelForm):
    # добавим согласие юзера с обр.перс.д.:
    personal_data = forms.BooleanField(label="Я согласен (/согласна) на обработку персональных данных.", required=True)
    # скроем возм.выбора дома:
    house = forms.ModelChoiceField(queryset=House.objects.all(), widget=forms.HiddenInput)
    # queryset в кач-ве фильтра, widget - настройка отображения
    # свяжем форму и модель:
    class Meta:
        model = Order
        # укажу поля, которые отобразить:
        fields = ["house", "name", "phone"]
        # id и date не указал, это поля, которые нужны мне (не клиенту)