__author__ = 'Administrator'

from .models import Users
from django.http import HttpResponseRedirect
from django.contrib.auth import SESSION_KEY
from urllib import quote

import datetime


class TokenAuthenticationMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print(request)
        path = request.path
        # if admin site, return position, others return None
        match1 = re.match("/admin/*", path, flags=0)
        match2 = re.match("/api/users/login", path, flags=0)
        # if not the admin site
        if match1 != None or match2 != None:
            response = self.get_response(request)
            return response
        if request.COOKIES.has_key("token") and request.COOKIES.has_key("userid"):
            cookietoken = request.COOKIES["token"]
            userid = request.COOKIES["userid"]
            user = Users.objects.filter(userid=userid,token=token)
            if user.count() != 1:
                result = {"code": 400, "message": "wrong userid or token"}
                return HttpResponse(json.dumps(result), content_type="application/json")
            elif user[0].token_expire_time >= datetime.datetime.now():
                result = {"code": 400, "message": "token expired, login required"}
                return HttpResponse(json.dumps(result), content_type="application/json")
            else:
                response = self.get_response(request)
                return response
        else:
            result = {"code": 400, "message": "token required"}
            return HttpResponse(json.dumps(result), content_type="application/json")