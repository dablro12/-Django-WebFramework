from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

# Create your views here.
# def index(request): #파라미터로 request를 받으면 아래의 Response로 응답
#     return render(
#         request = request,
#         template_name= 'foods/index.html', #<-- template내의 렌더링할 파일(index.html)로 지정해주기 
#         context = None,
#         content_type= 'text/html',
#         status= 200,
#     )
    
def index(request):
    context = {
        "date" : str(datetime.today().date())
    }

    return render(request, 'foods/index.html', context = context) #렌더함수에 특정 값을 dict형태로 보내서 사용할 수 있다.

def food_detail(request, food):
    context = dict()
    if food == "chicken":
        context['name'] = '코빠닭'
        context['description'] = "코빠닭은 맛있어요"
        context['price'] = 10000
        context["img_path"] = "foods/images/chicken.jpg"        
    return render(request, 'foods/detail.html', context = context)


def detail(request, menu):
    return render(request, 'foods/detial.html') 