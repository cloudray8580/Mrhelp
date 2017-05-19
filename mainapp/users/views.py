from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from mainapp.models import Users
from mainapp.serializers import SystemUserSerializer

@api_view(['GET','POST'])
@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = SystemUserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SystemUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def users_detail(request, userid):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        user = Users.objects.get(userid=userid)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SystemUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SystemUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
