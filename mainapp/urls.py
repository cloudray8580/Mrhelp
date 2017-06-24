__author__ = 'Administrator'


from django.conf.urls import url
from . import views
from django.conf.urls import include

from rest_framework.authtoken import views
urlpatterns = [
    #url(r'^test$', views.test, name='test'),
    url(r'^users/', include("mainapp.users.urls")),
    url(r'^missions/', include("mainapp.missions.urls")),
    url(r'^activities/', include("mainapp.activities.urls")),
    url(r'^adv/', include("mainapp.advertisements.urls"))
]