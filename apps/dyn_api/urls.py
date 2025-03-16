# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path
from apps.dyn_api import views 

urlpatterns = [
    path('api/', views.index, name="dynamic_api"),

    path('api/<str:model_name>/'          , views.DynamicAPI.as_view(), name="model_api"),
    path('api/<str:model_name>/<str:id>'  , views.DynamicAPI.as_view()),
    path('api/<str:model_name>/<str:id>/' , views.DynamicAPI.as_view()),
]
