from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    path('edit/', views.edit, name='edit'),
    path('personalinfo/', views.personalinfo, name="personalinfo"),
    path('member_del/', views.member_del, name='member_del'),
    # path('회원수정/', views.회원수정, name="회원수정"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)