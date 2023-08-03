from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_grouped_users, name='display_grouped_user'),
]