from django.urls import path
from account.views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [

path('sendNotification',sendNotification,name='sendNotification'),
]