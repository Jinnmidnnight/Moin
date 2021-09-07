from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('open_1', open_1, name="open_1"),
    path('index_1', index_1, name="index_1"),
    path('detail_1/<str:open_id>', detail_1, name="detail_1"),
    path('select', select, name="select"),
]

