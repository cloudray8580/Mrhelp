from __future__ import unicode_literals

from django.db import models

# Create your models here.

# aboout users

class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=True)
    address = models.TextField(null=True,blank=True)
    realname = models.CharField(max_length=200, null=True,blank=True)

    zone_choice = (
        (1,'86'),
        (2,'852'),
    )
    zone = models.IntegerField(choices=zone_choice, null=True,blank=True)
    mobile = models.CharField(max_length=200, null=True,blank=True)

    status_choice = (
        (1,'normal'),
        (2,'vip'),
        (3,'ban')
    )
    status = models.IntegerField(choices=status_choice, null=True,blank=True)

    head_image = models.ImageField(null=True,blank=True,upload_to="static/head/")

    token = models.CharField(max_length=100,null=True,blank=True)
    token_expire_time = models.DateTimeField(null=True,blank=True)
    register_time = models.DateTimeField(null=True,blank=True)
    register_ip = models.CharField(max_length=100,null=True,blank=True)
    last_login_time = models.DateTimeField(null=True,blank=True)
    last_login_ip = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.username

class ThirdPlatformAccount(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users,on_delete = models.CASCADE)
    accountid = models.CharField(max_length=200)
    accountname = models.CharField(max_length=200)
    account_type_choice = (
        (1,'wechat'),
        (2,'sina'),
        (3,'facebook')
    )
    account_type = models.IntegerField(choices=account_type_choice)

    def __str__(self):
        return self.userid + " " + self.accountid

# about mission
class Mission(models.Model):
    missionid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    context = models.TextField(null=True,blank=True)
    create_time = models.DateTimeField()
    close_time = models.DateTimeField(null=True,blank=True)
    reward = models.IntegerField(null=True,blank=True)
    payment_choice = (
        (1,'cash'),
        (2,'wechat'),
        (3,'alipay'),
        (4,'paypal'),
    )
    payment_method = models.IntegerField(choices=payment_choice,null=True,blank=True)
    type_choice =(
        (1,'comprehensive/others'),
        (2,'borrow/share'),
        (3,'lostandfound'),
        (4,'house renting'),
        (5,'delivery'),
        (6,'homework/study'),
        (7,'playing'),
        (8,'temamate/competition'),
        (9,'voting'),
        (10,'fixing'),
    )
    type = models.IntegerField(choices=type_choice)

    status_choice = (
        (1,'waiting'), # waiting some one to receive this order, or reopen this order
        (2,'processing'), # someone is handling this order
        (3, 'finishing'), # this mission is finished successfully
        (4, 'fail'), # this order closed by owner, or expire time
    )
    status = models.IntegerField(choices=status_choice)

    # naming strategy : 1~6_missionid
    description_picture1 = models.ImageField(null=True,blank=True, upload_to="static/mission/")
    description_picture2 = models.ImageField(null=True,blank=True, upload_to="static/mission/")
    description_picture3 = models.ImageField(null=True,blank=True, upload_to="static/mission/")
    description_picture4 = models.ImageField(null=True,blank=True, upload_to="static/mission/")
    description_picture5 = models.ImageField(null=True,blank=True, upload_to="static/mission/")
    description_picture6 = models.ImageField(null=True,blank=True, upload_to="static/mission/")

    owner_userid = models.ForeignKey(Users)
    receiver_userid = models.IntegerField(null=True,blank=True) # no allow to use foreign key here to User again

    def __str__(self):
        return str(self.missionid) + " " + self.title

class Chat(models.Model):
    chatid = models.AutoField(primary_key=True)
    content = models.TextField(null=True)
    image_content = models.ImageField(null=True, upload_to="static/chat/")
    from_userid = models.ForeignKey(Users,on_delete = models.CASCADE)
    to_userid = models.IntegerField() # no allow to use foreign key here to User again
    send_time = models.DateTimeField()

    def __str__(self):
        return str(self.chatid) + " " + self.content

class Activity(models.Model):
    activityid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    context = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField()
    close_time = models.DateTimeField(null=True, blank=True)
    activity_time = models.DateTimeField(null=True, blank=True)
    status_choice = (
        (1, 'on'),  # waiting some one to apply
        (2, 'close'),  # quota is full or time is passed
    )
    status = models.IntegerField(choices=status_choice)

    # naming strategy : 1~6_activityid
    description_picture1 = models.ImageField(null=True, blank=True, upload_to="static/activity/")
    description_picture2 = models.ImageField(null=True, blank=True, upload_to="static/activity/")
    description_picture3 = models.ImageField(null=True, blank=True, upload_to="static/activity/")
    description_picture4 = models.ImageField(null=True, blank=True, upload_to="static/activity/")
    description_picture5 = models.ImageField(null=True, blank=True, upload_to="static/activity/")
    description_picture6 = models.ImageField(null=True, blank=True, upload_to="static/activity/")

    creater_userid = models.ForeignKey(Users)

class Advertisement(models.Model):
    advid = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(null=True,blank=True)
    title = models.CharField(max_length=50)
    # naming strategy : 1~6_advid
    description_picture = models.ImageField(null=True, blank=True, upload_to="static/homeadv/")
    type_choice = (
        (1, 'mission'),
        (2, 'activity'),
        (3, 'others')
    )
    type = models.IntegerField(choices=type_choice)

    missionid = models.ForeignKey(Mission)
    activityid = models.ForeignKey(Activity)


