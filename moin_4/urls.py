from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_4', open_4, name="open_4"),
    path('index_4', index_4, name="index_4"),
    path('index_4_1', index_4_1, name="index_4_1"),
    path('detail_4/<str:open_id>/', detail_4, name="detail_4"),
    path('like_4/<str:open_id>/', likes_4, name="likes_4"),
    path('follow_4/<str:open_id>/', follow_4, name="follow_4"),

    path('write_4/<str:open_id>/', write_4, name="write_4"),
    path('comment_4/<str:write_id>/', comment_4, name="comment_4"),
    path('add_comment_4/<str:write_id>/', add_comment_4, name="add_comment_4"),
    path('write_like_4/<str:write_id>/', write_like_4, name="write_like_4"),

    path('update_4/<str:open_id>/', update_4, name="update_4"),
    path('delete_alert_4/<str:open_id>/', delete_alert_4, name="delete_alert_4"),
    path('delete_4/<str:open_id>/', delete_4, name="delete_4"),

    path('write_update_4/<str:open_id>/<str:write_id>/', write_update_4, name="write_update_4"),
    path('write_delete_4/<str:write_id>/', write_delete_4, name="write_delete_4"),
    path('comment_delete_4/<str:comment_id>/',comment_delete_4,name="comment_delete_4"),

    path('deport_alert_4/<str:open_id>/', deport_alert_4, name="deport_alert_4"),
    path('deport_4/<str:open_id>/', deport_4, name="deport_4"),
    ]