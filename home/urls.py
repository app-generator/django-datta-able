from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
  IndexTemplateView,
  TablesTemplateView
)

urlpatterns = [
  path('', IndexTemplateView.as_view(),  name='index'),
  path('tables/', TablesTemplateView.as_view(), name='tables'),
]
