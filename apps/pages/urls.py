from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('', views.index,  name='index'),
  path('charts/', views.charts,  name='charts'),
]
