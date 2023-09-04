from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_9', open_9, name="open_9"),
    path('index_9', index_9, name="index_9"),
    path('index_9_1', index_9_1, name="index_9_1"),
    path('detail_9/<str:open_id>/', detail_9, name="detail_9"),
    path('like_9/<str:open_id>/', likes_9, name="likes_9"),
    path('follow_9/<str:open_id>/', follow_9, name="follow_9"),

    path('write_9/<str:open_id>/', write_9, name="write_9"),
    path('comment_9/<str:write_id>/', comment_9, name="comment_9"),
    path('add_comment_9/<str:write_id>/', add_comment_9, name="add_comment_9"),
    path('write_like_9/<str:write_id>/', write_like_9, name="write_like_9"),

    path('update_9/<str:open_id>/', update_9, name="update_9"),
    path('delete_alert_9/<str:open_id>/', delete_alert_9, name="delete_alert_9"),
    path('delete_9/<str:open_id>/', delete_9, name="delete_9"),

    path('write_update_9/<str:open_id>/<str:write_id>/', write_update_9, name="write_update_9"),
    path('write_delete_9/<str:write_id>/', write_delete_9, name="write_delete_9"),
    path('comment_delete_9/<str:comment_id>/',comment_delete_9,name="comment_delete_9"),

    path('deport_alert_9/<str:open_id>/', deport_alert_9, name="deport_alert_9"),
    path('deport_9/<str:open_id>/', deport_9, name="deport_9"),
    ]