from django.db import models
# импортирую модель приложения House:
from houses.models import House

# создаю внешний ключ на дом = модель Order связана с House,
# заявка б/т хранить идент-р дома, к к-му заявка отн-ся.
class Order(models.Model):
    house = models.ForeignKey(House, verbose_name="дом", on_delete=models.CASCADE)
    # on_delete - при удалении дома удаляются заявки этого дома
    #добавлю поле name для имени потенц.клиента:
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    # дата заявки автоматически б/т заполнено актуальн. датой:
    date = models.DateTimeField("дата", auto_now_add=True)

    # сделаю в админке "заявка\-ки" вместо "order\-s":
    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"


