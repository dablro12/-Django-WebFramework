from django.contrib import admin
from django.urls import path
from . import views 

"""
urlpattenrs: url에 base 부분이 바귈때 어떻게 조치할지 볼 수 있음
"""
urlpatterns = [
    path('index/', views.index),
    path('menu/<str:food>/', views.food_detail), #8000:/foods/menu/{음식}이 들어오면 views 파일의 함수(food_detail)를 실행하도록 함.
    
]
