from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index (request):
    # return HttpResponse("<h1>hello</h1>")
    print(request,'pages/index.html')
    return render(request, 'pages/index.html')


def about (request):
    print(request,'pages/about.html')
    return render(request,'pages/about.html')

