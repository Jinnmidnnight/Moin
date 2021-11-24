from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('select', select, name="select"),
    path('open_1', open_1, name="open_1"),
    path('index_1', index_1, name="index_1"),
    path('detail_1/<str:open_id>', detail_1, name="detail_1"),
    path('join_1/<str:open_id>', join_1, name="join_1"),
    path('open_2', open_2, name="open_2"),
    path('index_2', index_2, name="index_2"),
    path('detail_2/<str:open_id>', detail_2, name="detail_2"),
    path('open_3', open_3, name="open_3"),
    path('index_3', index_3, name="index_3"),
    path('detail_3/<str:open_id>', detail_3, name="detail_3"),
    path('open_4', open_4, name="open_4"),
    path('index_4', index_4, name="index_4"),
    path('detail_4/<str:open_id>', detail_4, name="detail_4"),
    path('open_5', open_5, name="open_5"),
    path('index_5', index_5, name="index_5"),
    path('detail_5/<str:open_id>', detail_5, name="detail_5"),
    path('open_6', open_6, name="open_6"),
    path('index_6', index_6, name="index_6"),
    path('detail_6/<str:open_id>', detail_6, name="detail_6"),
    path('open_7', open_7, name="open_7"),
    path('index_7', index_7, name="index_7"),
    path('detail_7/<str:open_id>', detail_7, name="detail_7"),
    path('open_8', open_8, name="open_8"),
    path('index_8', index_8, name="index_8"),
    path('detail_8/<str:open_id>', detail_8, name="detail_8"),
    path('open_9', open_9, name="open_9"),
    path('index_9', index_9, name="index_9"),
    path('detail_9/<str:open_id>', detail_9, name="detail_9"),

    path('like_1/<str:open_id>/', likes_1, name="likes_1"),
    path('like_2/<str:open_id>/', likes_2, name="likes_2"),
    path('like_3/<str:open_id>/', likes_3, name="likes_3"),
    path('like_4/<str:open_id>/', likes_4, name="likes_4"),
    path('like_5/<str:open_id>/', likes_5, name="likes_5"),
    path('like_6/<str:open_id>/', likes_6, name="likes_6"),
    path('like_7/<str:open_id>/', likes_7, name="likes_7"),
    path('like_8/<str:open_id>/', likes_8, name="likes_8"),
    path('like_9/<str:open_id>/', likes_9, name="likes_9"),



]

