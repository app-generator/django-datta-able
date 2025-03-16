from django.urls import path
from apps.dyn_dt import views 

urlpatterns = [
    path('dynamic-dt/', views.index, name="dynamic_dt"),

    path('create-filter/<str:model_name>/', views.create_filter, name="create_filter"),
    path('create-page-items/<str:model_name>/', views.create_page_items, name="create_page_items"),
    path('create-hide-show-items/<str:model_name>/', views.create_hide_show_filter, name="create_hide_show_filter"),
    path('delete-filter/<str:model_name>/<int:id>/', views.delete_filter, name="delete_filter"),
    path('create/<str:aPath>/', views.create, name="create"),
    path('delete/<str:aPath>/<int:id>/', views.delete, name="delete"),
    path('update/<str:aPath>/<int:id>/', views.update, name="update"),

    path('export-csv/<str:aPath>/', views.ExportCSVView.as_view(), name='export_csv'),

    path('dynamic-dt/<str:aPath>/', views.model_dt, name="model_dt"),
]
