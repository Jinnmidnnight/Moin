from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_7', open_7, name="open_7"),
    path('index_7', index_7, name="index_7"),
    path('index_7_1', index_7_1, name="index_7_1"),
    path('detail_7/<str:open_id>/', detail_7, name="detail_7"),
    path('like_7/<str:open_id>/', likes_7, name="likes_7"),
    path('follow_7/<str:open_id>/', follow_7, name="follow_7"),

    path('write_7/<str:open_id>/', write_7, name="write_7"),
    path('comment_7/<str:write_id>/', comment_7, name="comment_7"),
    path('add_comment_7/<str:write_id>/', add_comment_7, name="add_comment_7"),
    path('write_like_7/<str:write_id>/', write_like_7, name="write_like_7"),

    path('update_7/<str:open_id>/', update_7, name="update_7"),
    path('delete_alert_7/<str:open_id>/', delete_alert_7, name="delete_alert_7"),
    path('delete_7/<str:open_id>/', delete_7, name="delete_7"),

    path('write_update_7/<str:open_id>/<str:write_id>/', write_update_7, name="write_update_7"),
    path('write_delete_7/<str:write_id>/', write_delete_7, name="write_delete_7"),
    path('comment_delete_7/<str:comment_id>/',comment_delete_7,name="comment_delete_7"),

    path('deport_alert_7/<str:open_id>/', deport_alert_7, name="deport_alert_7"),
    path('deport_7/<str:open_id>/', deport_7, name="deport_7"),
    ]