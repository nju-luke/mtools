from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from monitor.models import StockPrice

# Create your views here.

import hashlib
import json


def index(request):
    # print(request)

    # echostr = request.GET['echostr']

    # return echostr

    # return HttpResponse("Hello, world. You're at the monitor index.")
    return render(request, "index.html")


# def checkSignature(request):
#     signature = request.GET['signature']
#     timestamp = request.GET['timestamp']
#     nonce = request.GET['nonce']
#
#     token = 'shsptqgluqj6c50h601'
#
#     arrs = sorted(token, timestamp, nonce)
#     str_arrs = "".join(arrs)
#     sig = hashlib.sha1(str_arrs)
#
#     print(sig)
#     if sig == signature:
#         return True
#     else:
#         return False

@login_required
def mainpg(request):
    # return HttpResponse("Hello, world. You're at the monitor index1.")

    return render(request, "../templates/show.html")


@login_required
def create_data(request):
    try:
        values = request.POST
        username = request.user.username
        StockPrice.objects.update_or_create(code=values['Code'], name=values["name"], vi2=values["vi2"],
                                            vi1=values["vi1"], v0=values["v0"],
                                            vh1=values["vh1"], vh2=values["vh2"],
                                            vcur=values["vcur"], username=username)
    except ValueError:
        return HttpResponse("请正确输入！")

    return HttpResponse("OK")


def get_data(request):
    username = request.user.username
    if username == "":
        username = "bianseyang"
    values = StockPrice.objects.filter(username=username)
    data = []
    for v in values.values():
        v.pop("username")
        data.append(v)


    # item = StockPrice.objects.filter(name="洋河").values()[0]
    res = {"data": data}


    # return HttpResponse(json.dumps(res), content_type="application/json")
    return JsonResponse(res, safe=False)
