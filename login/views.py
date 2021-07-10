from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
import json

# from login.models import User
from django.views.generic.base import View

times = 0

class SignIn(View):
    def get(self, request, *args, **kwargs):

        report_loc = '/accounts/signin/'
        return render(request, 'login.html', {'loc':report_loc,'error': ''})

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/mainpg")
        report_loc = '/accounts/signin/'
        return render(request, 'login.html', {'loc': report_loc, 'error': '用户名或密码错误！'})

