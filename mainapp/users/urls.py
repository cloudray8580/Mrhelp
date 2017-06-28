__author__ = 'Administrator'


from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.users_list),
    # url(r'^(?P<userid>[0-9]+)$',views.users_detail)
    url(r'^login$', views.login),
    url(r'^$', views.UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
]