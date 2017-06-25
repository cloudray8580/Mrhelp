from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from mainapp.models import Mission
from mainapp.serializers import MissionSerializer
from rest_framework import generics


from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.decorators import authentication_classes
class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class MissionList(generics.ListCreateAPIView):
    authenticaiton_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    authenticaiton_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


# @api_view(['GET','POST'])
# @csrf_exempt
# @authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
# def missions_list(request):
#     """
#     Retrieve, create a mission list.
#     start from /api/
#     """
#     if request.method == 'GET':
#         missions = Mission.objects.all()
#         serializer = MissionSerializer(missions, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MissionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# @authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
# def missions_detail(request, missionid):
#     """
#     Retrieve, update or delete a mission instance.
#     start from /api/
#     """
#     try:
#         mission = Mission.objects.get(missionid=missionid)
#     except Mission.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = MissionSerializer(mission)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = MissionSerializer(mission, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         mission.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)