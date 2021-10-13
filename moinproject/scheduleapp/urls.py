from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('schedule_1/<str:open_id>', schedule_1, name="schedule_1"),
]
