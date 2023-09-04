from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('open_2', open_2, name="open_2"),
    path('index_2', index_2, name="index_2"),
    path('index_2_1', index_2_1, name="index_2_1"),
    path('detail_2/<str:open_id>/', detail_2, name="detail_2"),
    path('like_2/<str:open_id>/', likes_2, name="likes_2"),
    path('follow_2/<str:open_id>/', follow_2, name="follow_2"),

    path('write_2/<str:open_id>/', write_2, name="write_2"),
    path('comment_2/<str:write_id>/', comment_2, name="comment_2"),
    path('add_comment_2/<str:write_id>/', add_comment_2, name="add_comment_2"),
    path('write_like_2/<str:write_id>/', write_like_2, name="write_like_2"),

    path('update_2/<str:open_id>/', update_2, name="update_2"),
    path('delete_alert_2/<str:open_id>/', delete_alert_2, name="delete_alert_2"),
    path('delete_2/<str:open_id>/', delete_2, name="delete_2"),

    path('write_update_2/<str:open_id>/<str:write_id>/', write_update_2, name="write_update_2"),
    path('write_delete_2/<str:write_id>/', write_delete_2, name="write_delete_2"),
    path('comment_delete_2/<str:comment_id>/',comment_delete_2,name="comment_delete_2"),

    path('deport_alert_2/<str:open_id>/', deport_alert_2, name="deport_alert_2"),
    path('deport_2/<str:open_id>/', deport_2, name="deport_2"),
    ]