__author__ = 'Administrator'


from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns = [
    url(r'^test$', views.test, name='test')
]