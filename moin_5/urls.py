from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_5', open_5, name="open_5"),
    path('index_5', index_5, name="index_5"),
    path('index_5_1', index_5_1, name="index_5_1"),
    path('detail_5/<str:open_id>/', detail_5, name="detail_5"),
    path('like_5/<str:open_id>/', likes_5, name="likes_5"),
    path('follow_5/<str:open_id>/', follow_5, name="follow_5"),

    path('write_5/<str:open_id>/', write_5, name="write_5"),
    path('comment_5/<str:write_id>/', comment_5, name="comment_5"),
    path('add_comment_5/<str:write_id>/', add_comment_5, name="add_comment_5"),
    path('write_like_5/<str:write_id>/', write_like_5, name="write_like_5"),

    path('update_5/<str:open_id>/', update_5, name="update_5"),
    path('delete_alert_5/<str:open_id>/', delete_alert_5, name="delete_alert_5"),
    path('delete_5/<str:open_id>/', delete_5, name="delete_5"),

    path('write_update_5/<str:open_id>/<str:write_id>/', write_update_5, name="write_update_5"),
    path('write_delete_5/<str:write_id>/', write_delete_5, name="write_delete_5"),
    path('comment_delete_5/<str:comment_id>/',comment_delete_5,name="comment_delete_5"),

    path('deport_alert_5/<str:open_id>/', deport_alert_5, name="deport_alert_5"),
    path('deport_5/<str:open_id>/', deport_5, name="deport_5"),
    ]