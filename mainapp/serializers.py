from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

# that's our own user
class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('userid','username','password','email','address','realname',
                  'zone','mobile','status','head_image','token','token_expire_time',
                  'register_time','register_ip','last_login_time','last_login_ip')

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('missionid','title','context','create_time','close_time',
                  'reward','payment_method','type','status','description_picture1',
                  'description_picture2','description_picture3','description_picture4',
                  'description_picture5','description_picture6','owner_userid','receiver_userid')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activityid','title','context','create_time','close_time',
                  'activity_time','status','description_picture1',
                  'description_picture2','description_picture3','description_picture4',
                  'description_picture5','description_picture6','creater_userid')

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('advid','update_time','title','description_picture','type','missionid','activityid')