from django.urls import path
from mypageapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('update_1/<str:open_id>', update_1, name="update_1"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)