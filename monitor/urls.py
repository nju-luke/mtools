# -*- coding:utf-8 -*-
"""
author: Luke
datettime: 2021/7/3 20:27
"""


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mainpg', views.mainpg, name='mainpg'),
    path('create_data/', views.create_data, name='create_data'),
    path('get_data/', views.get_data, name='get_data'),
]