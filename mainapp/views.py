from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
def test(request):
    response_data = {}
    response_data['code'] = "200"
    response_data['msg'] = "success"
    return HttpResponse(json.dumps(response_data), content_type="application/json")

