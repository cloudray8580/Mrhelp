__author__ = 'Administrator'


from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ActivityList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.ActivityDetail.as_view())
]