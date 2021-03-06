from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from mainapp.models import Advertisement
from mainapp.serializers import AdvertisementSerializer
from rest_framework import generics

from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.decorators import authentication_classes
class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class AdvertisementList(generics.ListCreateAPIView):
    authenticaiton_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementDetail(generics.RetrieveUpdateDestroyAPIView):
    authenticaiton_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
