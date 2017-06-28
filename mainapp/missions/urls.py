__author__ = 'Administrator'


from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.missions_list),
    # url(r'^(?P<missionid>[0-9]+)$',views.missions_detail)
    url(r'^$', views.MissionList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.MissionDetail.as_view())
]