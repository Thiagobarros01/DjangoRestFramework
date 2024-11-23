from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.get_users , name= 'api_name_urls')
]