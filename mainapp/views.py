from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


from django.http import HttpResponse
import json
def test(request):
    response_data = {}
    response_data['code'] = "200"
    response_data['msg'] = "success"
    return HttpResponse(json.dumps(response_data), content_type="application/json")

