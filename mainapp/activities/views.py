from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from mainapp.models import Activity
from mainapp.serializers import ActivitySerializer
from rest_framework import generics

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# from rest_framework.decorators import authentication_classes
# class CsrfExemptSessionAuthentication(SessionAuthentication):
#
#     def enforce_csrf(self, request):
#         return  # To not perform the csrf check previously happening
#
