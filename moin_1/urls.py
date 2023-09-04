from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_1', open_1, name="open_1"),
    path('index_1', index_1, name="index_1"),
    path('index_1_1', index_1_1, name="index_1_1"),
    path('detail_1/<str:open_id>/', detail_1, name="detail_1"),
    path('like_1/<str:open_id>/', likes_1, name="likes_1"),
    path('follow_1/<str:open_id>/', follow_1, name="follow_1"),

    path('write_1/<str:open_id>/', write_1, name="write_1"),
    path('comment_1/<str:write_id>/', comment_1, name="comment_1"),
    path('add_comment_1/<str:write_id>/', add_comment_1, name="add_comment_1"),
    path('write_like_1/<str:write_id>/', write_like_1, name="write_like_1"),

    path('update_1/<str:open_id>/', update_1, name="update_1"),
    path('delete_alert_1/<str:open_id>/', delete_alert_1, name="delete_alert_1"),
    path('delete_1/<str:open_id>/', delete_1, name="delete_1"),

    path('write_update_1/<str:open_id>/<str:write_id>/', write_update_1, name="write_update_1"),
    path('write_delete_1/<str:write_id>/', write_delete_1, name="write_delete_1"),
    path('comment_delete_1/<str:comment_id>/',comment_delete_1,name="comment_delete_1"),

    path('deport_alert_1/<str:open_id>/', deport_alert_1, name="deport_alert_1"),
    path('deport_1/<str:open_id>/', deport_1, name="deport_1"),
    ]