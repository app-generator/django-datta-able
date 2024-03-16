from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('sample-page/', views.scan, name='scan'),
  path('sub_scan/', views.sub_scan, name='sub_scan'),
]
