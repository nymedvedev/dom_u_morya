# ФАЙЛ С URL ПРОЕКТА

"""
URL configuration for dom_u_morya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# импортируем наше представление,
# h_list для списка домов, h_detail - для стр. с отд.домом:
from houses.views import houses_list, house_detail
# импортируем функцию static, отв. за обраб. статич. файлов(контента):
from django.conf.urls.static import static
# импортируем наши настройки:
from django.conf import settings


# настройки панели админки, доб. автоматически при созд. проекта
urlpatterns = [
    path('admin/', admin.site.urls),
    # настройки, доб. мной для представления:
    path('', houses_list, name="home"),
    # '' - пустая строка отв. за главную стр.,
    # houses_list - стр., которая б/т вызываться, когда юзер откр. глав.стр.
    # для отобр. стр. с url = номеру дома:
    path("<int:house_id>", house_detail, name="house")
]
# подключим обработку файлов: свяжем URL MEDIA в бр-ре и на ж.диске,
# чтобы не использ. представление, а отдавать файлы как есть (статич.контент)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
