# ФАЙЛ ДЛЯ СОЗДАНИЯ ФИЛЬТРОВ ДЛЯ СТР.С ДОМАМИ
from django import forms

# создадим форму не на осн. модели, а простую, для ручн.редактирования
class HousesFilterForm(forms.Form):
    # пропишем фильтры
    min_price = forms.IntegerField(label="от", required=False)
    # IntegerField - прин.целые числа, label - назв.поля,
    # required=False - значит данные можно не заполнять
    max_price = forms.IntegerField(label="до", required=False)
    # добавлю форму поиска по тексту:
    query = forms.CharField(label="описание", required=False)
