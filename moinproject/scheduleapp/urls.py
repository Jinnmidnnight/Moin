from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('schedule_1/<str:open_id>', schedule_1, name="schedule_1"),
    path('schedule_make/<str:open_id>', schedule_make, name="schedule_make"),
    path('schedule_making/<str:open_id>', schedule_making, name="schedule_making"),
]
