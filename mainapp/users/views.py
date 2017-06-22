from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from mainapp.models import Users
from mainapp.serializers import SystemUserSerializer

from rest_framework import generics


# from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# from rest_framework.decorators import authentication_classes
# class CsrfExemptSessionAuthentication(SessionAuthentication):
#
#     def enforce_csrf(self, request):
#         return  # To not perform the csrf check previously happening

class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = SystemUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = SystemUserSerializer

import datetime
import time
import os
import hashlib
from django.http import HttpResponse
import json
@api_view(['POST'])
def login(request):
    if request.POST.has_key('email'):
        email = request.POST["email"]
        user = Users.objects.filter(email=email)
        if user.count() == 0:
            result = {"code": 400, "message": "invalid user email"}
            return HttpResponse(json.dumps(result), content_type="application/json")

    else:
        result = {"code":400, "message":"missing user email"}
        return HttpResponse(json.dumps(result), content_type="application/json")

    if request.POST.has_key('password'):
        password = request.POST["password"]
        if password == user[0].password:
            token = hashlib.sha1(os.urandom(24)).hexdigest()
            user.update(token=token)
            time = datetime.datetime.now()
            time = time + datetime.timedelta(seconds=3600*24*7)
            user.update(token_expire_time=time)
            result = {"code": 200, "token": token,"expire":str(time)}
            return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            result = {"code": 400, "message": "wrong password"}
            return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        result = {"code": 400, "message": "missing user password"}
        return HttpResponse(json.dumps(result), content_type="application/json")


# @api_view(['GET','POST'])
# @csrf_exempt
# @authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
# def users_list(request):
#     """
#     Retrieve, create a user list.
#     start from /api/
#     """
#     if request.method == 'GET':
#         users = Users.objects.all()
#         serializer = SystemUserSerializer(users, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SystemUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# @authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
# def users_detail(request, userid):
#     """
#     Retrieve, update or delete a user instance.
#     start from /api/
#     """
#     try:
#         user = Users.objects.get(userid=userid)
#     except Users.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SystemUserSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SystemUserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
