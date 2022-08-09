# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # The home page
    path('', login_required(TemplateView.as_view(template_name='home/index.html',)), name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
