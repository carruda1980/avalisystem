from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
