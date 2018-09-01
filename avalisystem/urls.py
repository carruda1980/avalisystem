from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
]
