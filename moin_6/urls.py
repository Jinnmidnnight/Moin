from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_6', open_6, name="open_6"),
    path('index_6', index_6, name="index_6"),
    path('index_6_1', index_6_1, name="index_6_1"),
    path('detail_6/<str:open_id>/', detail_6, name="detail_6"),
    path('like_6/<str:open_id>/', likes_6, name="likes_6"),
    path('follow_6/<str:open_id>/', follow_6, name="follow_6"),

    path('write_6/<str:open_id>/', write_6, name="write_6"),
    path('comment_6/<str:write_id>/', comment_6, name="comment_6"),
    path('add_comment_6/<str:write_id>/', add_comment_6, name="add_comment_6"),
    path('write_like_6/<str:write_id>/', write_like_6, name="write_like_6"),

    path('update_6/<str:open_id>/', update_6, name="update_6"),
    path('delete_alert_6/<str:open_id>/', delete_alert_6, name="delete_alert_6"),
    path('delete_6/<str:open_id>/', delete_6, name="delete_6"),

    path('write_update_6/<str:open_id>/<str:write_id>/', write_update_6, name="write_update_6"),
    path('write_delete_6/<str:write_id>/', write_delete_6, name="write_delete_6"),
    path('comment_delete_6/<str:comment_id>/',comment_delete_6,name="comment_delete_6"),

    path('deport_alert_6/<str:open_id>/', deport_alert_6, name="deport_alert_6"),
    path('deport_6/<str:open_id>/', deport_6, name="deport_6"),
    ]