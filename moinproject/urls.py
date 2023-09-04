"""moinproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from moinapp.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('search/', search, name="search"),
    path('select/', select, name="select"),
    path('mypage/', mypage, name="mypage"),
    path('account/', include('account.urls')),
    path('moin_1/', include('moin_1.urls')),
    path('moin_2/', include('moin_2.urls')),
    path('moin_3/', include('moin_3.urls')),
    path('moin_4/', include('moin_4.urls')),
    path('moin_5/', include('moin_5.urls')),
    path('moin_6/', include('moin_6.urls')),
    path('moin_7/', include('moin_7.urls')),
    path('moin_8/', include('moin_8.urls')),
    path('moin_9/', include('moin_9.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
