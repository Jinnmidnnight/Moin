from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('write_1/<str:open_id>', write_1, name="write_1"),
    path('comment_1/<str:write_id>', comment_1, name="comment_1"),
]
