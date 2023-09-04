from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_3', open_3, name="open_3"),
    path('index_3', index_3, name="index_3"),
    path('index_3_1', index_3_1, name="index_3_1"),
    path('detail_3/<str:open_id>/', detail_3, name="detail_3"),
    path('like_3/<str:open_id>/', likes_3, name="likes_3"),
    path('follow_3/<str:open_id>/', follow_3, name="follow_3"),

    path('write_3/<str:open_id>/', write_3, name="write_3"),
    path('comment_3/<str:write_id>/', comment_3, name="comment_3"),
    path('add_comment_3/<str:write_id>/', add_comment_3, name="add_comment_3"),
    path('write_like_3/<str:write_id>/', write_like_3, name="write_like_3"),

    path('update_3/<str:open_id>/', update_3, name="update_3"),
    path('delete_alert_3/<str:open_id>/', delete_alert_3, name="delete_alert_3"),
    path('delete_3/<str:open_id>/', delete_3, name="delete_3"),

    path('write_update_3/<str:open_id>/<str:write_id>/', write_update_3, name="write_update_3"),
    path('write_delete_3/<str:write_id>/', write_delete_3, name="write_delete_3"),
    path('comment_delete_3/<str:comment_id>/',comment_delete_3,name="comment_delete_3"),

    path('deport_alert_3/<str:open_id>/', deport_alert_3, name="deport_alert_3"),
    path('deport_3/<str:open_id>/', deport_3, name="deport_3"),
    ]