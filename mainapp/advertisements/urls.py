__author__ = 'Administrator'


from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.AdvertisementList.as_view()),
    url(r'^(?P<activityid>[0-9]+)$',views.AdvertisementDetail.as_view())
]