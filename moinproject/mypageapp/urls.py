from django.urls import path
from mypageapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('manage_1/<str:open_id>', manage_1, name="manage_1"),
    path('manage_2/<str:open_id>', manage_2, name="manage_2"),
    path('deport_1/<str:open_id>', deport_1, name="deport_1"),
    path('update_1/<str:open_id>', update_1, name="update_1"),
    path('delete_1/<str:open_id>', delete_1, name="delete_1"),
    path('write_delete_1/<str:write_id>/', write_delete_1, name="write_delete_1"),
    path('joinin/<str:open_id>', joinin, name="joinin"),
    path('joinin_wait/<str:open_id>', joinin_wait, name="joinin_wait"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)