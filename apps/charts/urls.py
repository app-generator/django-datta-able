from django.urls import path

from apps.charts import views

urlpatterns = [
    path("", views.index, name="charts"),
]