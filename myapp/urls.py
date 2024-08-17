from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.create, name='create_app'),
    path('app/<int:app_id>/', views.dispatcher, name='get_app'),
    path('apps/', views.list, name='list_apps'),
    # path('app/<int:app_id>/', views.update, name='update_app'),
    # path('app/<int:app_id>/', views.delete, name='delete_app'),
]