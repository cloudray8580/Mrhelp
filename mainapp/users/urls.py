__author__ = 'Administrator'


from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.users_list),
    url(r'^(?P<userid>[0-9]+)$',views.users_detail)
]