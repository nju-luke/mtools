# -*- coding:utf-8 -*-
"""
author: Luke
datettime: 2021/7/3 20:27
"""


from django.urls import path

from . import views, views_register

urlpatterns = [
    # path('', views.index, name='index'),

    # path('', views.index),
    # path('signin/', views.signin),
    path('', views.SignIn.as_view(), name='signin'),
    path('signin/', views.SignIn.as_view(), name='signin'),

    # path('register/', views_register.register),
    # path('signup/', views_register.signup),
    path('signup/', views_register.SignUp.as_view(), name='signup')
]