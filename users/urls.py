from django.conf.urls import url
from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns=[
    path('login/', obtain_auth_token, name='obtain_auth_token'),
    path('users/', users_operations, name='users_operations'),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>', users_modification, name='users_modification'),


]
