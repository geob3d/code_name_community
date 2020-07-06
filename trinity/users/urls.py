from django.urls import path
from . import views

urlpatterns = [
    path('trinity/users/', views.userListCreate.as_view() ),


]