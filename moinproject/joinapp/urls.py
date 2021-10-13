from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('joinin_wait', joinin_wait, name="joinin_wait"),
    path('joinin', joinin, name="joinin"),
    path('alert_approval', alert_approval, name="alert_approval"),
    path('alert_detail', alert_detail, name="alert_detail"),
    path('alert', alert, name="alert"),
    path('mygroup', mygroup, name="mygroup"),
]