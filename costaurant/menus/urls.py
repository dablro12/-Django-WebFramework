from django.contrib import admin
from django.urls import path
from . import views 

"""
urlpattenrs: url에 base 부분이 바귈때 어떻게 조치할지 볼 수 있음
"""
urlpatterns = [
    path('', views.index),
    path('menu/<str:menu>/', views.detail)
]
