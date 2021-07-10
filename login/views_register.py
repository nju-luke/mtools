from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import resolve
from django.views.generic import View
import json
times = 0


class SignUp(View):
    def get(self, request, *args, **kwargs):
        global times
        print('Register Page Opened!')
        times += 1
        current_url = request.path
        print(current_url)
        print(0)

        report_loc = '/accounts/signup/'
        return render(request, 'register.html', {'loc':report_loc,'error': ''})

    def post(self, request, *args, **kwargs):

        report_loc = '/accounts/signup/'


        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password != password1:
            print('Passwords do not match, returning HTTP response')
            return render(request, 'register.html', {'loc': report_loc, 'errorclass': 'alert alert-danger',
                                                     'error': 'Sorry. The Passwords do not match.'})
        # 判断用户名是否存在
        user = User.objects.filter(username=username)
        user = user if user else User.objects.filter(email=email)
        if user:
            print('The Username or Email ID is already taken, returning HTTP response')
            return render(request, 'register.html', {'loc':report_loc,'errorclass':'alert alert-danger','error': 'Sorry. The Username or Email ID is already taken.'})


        # 注册用户，返回主页

        user=User.objects.create_user(username=username, password=password, email=email)


        auth.login(request, user)
        return HttpResponseRedirect("/mainpg")





