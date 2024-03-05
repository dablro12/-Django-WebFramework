from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h2>정답입니다!</h2>")

def index(request):
    return render(request, 'index.html') #서로 index.html이 겹치지 않게 하기