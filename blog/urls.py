# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 08:58:11 2021

@author: Laurine
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]