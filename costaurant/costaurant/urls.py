"""
URL configuration for costaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

"""
urlpattenrs: url에 base 부분이 바귈때 어떻게 조치할지 볼 수 있음
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foods.urls')), #기본 웹페이지를 foods 앱으로 설정 
    path('foods/', include('foods.urls')), #foods앱에 foods앱안에 urls를 참조하도록 함.
    path('menus/', include('menus.urls')), #menus앱에 menus앱안에 urls를 참조하도록 함.
    path('greetings/', include('greetings.urls')), #foods앱에 foods앱안에 urls를 참조하도록 함.
    
]
