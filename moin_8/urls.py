from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_8', open_8, name="open_8"),
    path('index_8', index_8, name="index_8"),
    path('index_8_1', index_8_1, name="index_8_1"),
    path('detail_8/<str:open_id>/', detail_8, name="detail_8"),
    path('like_8/<str:open_id>/', likes_8, name="likes_8"),
    path('follow_8/<str:open_id>/', follow_8, name="follow_8"),

    path('write_8/<str:open_id>/', write_8, name="write_8"),
    path('comment_8/<str:write_id>/', comment_8, name="comment_8"),
    path('add_comment_8/<str:write_id>/', add_comment_8, name="add_comment_8"),
    path('write_like_8/<str:write_id>/', write_like_8, name="write_like_8"),

    path('update_8/<str:open_id>/', update_8, name="update_8"),
    path('delete_alert_8/<str:open_id>/', delete_alert_8, name="delete_alert_8"),
    path('delete_8/<str:open_id>/', delete_8, name="delete_8"),

    path('write_update_8/<str:open_id>/<str:write_id>/', write_update_8, name="write_update_8"),
    path('write_delete_8/<str:write_id>/', write_delete_8, name="write_delete_8"),
    path('comment_delete_8/<str:comment_id>/',comment_delete_8,name="comment_delete_8"),

    path('deport_alert_8/<str:open_id>/', deport_alert_8, name="deport_alert_8"),
    path('deport_8/<str:open_id>/', deport_8, name="deport_8"),
    ]