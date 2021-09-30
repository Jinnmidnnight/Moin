from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('write_1/<str:open_id>', write_1, name="write_1"),
    path('comment_1/<str:write_id>', comment_1, name="comment_1"),
    path('write_2/<str:open_id>', write_2, name="write_2"),
    path('comment_2/<str:write_id>', comment_2, name="comment_2"),
    path('write_3/<str:open_id>', write_3, name="write_3"),
    path('comment_3/<str:write_id>', comment_3, name="comment_3"),
    path('write_4/<str:open_id>', write_4, name="write_4"),
    path('comment_4/<str:write_id>', comment_4, name="comment_4"),
    path('write_5/<str:open_id>', write_5, name="write_5"),
    path('comment_5/<str:write_id>', comment_5, name="comment_5"),
    path('write_6/<str:open_id>', write_6, name="write_6"),
    path('comment_6/<str:write_id>', comment_6, name="comment_6"),
    path('write_7/<str:open_id>', write_7, name="write_7"),
    path('comment_7/<str:write_id>', comment_7, name="comment_7"),
    path('write_8/<str:open_id>', write_8, name="write_8"),
    path('comment_8/<str:write_id>', comment_8, name="comment_8"),
    path('write_9/<str:open_id>', write_9, name="write_9"),
    path('comment_9/<str:write_id>', comment_9, name="comment_9"),
]
