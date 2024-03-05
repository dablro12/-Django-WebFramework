from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #파라미터로 request를 받으면 아래의 Response로 응답
    return render(
        request = request,
        template_name= 'menus/index.html', #<-- template내의 렌더링할 파일(index.html)로 지정해주기 
        context = None,
        content_type= 'text/html',
        status= 200,
    )