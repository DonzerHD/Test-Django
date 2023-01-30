from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")
     
def article1(request):
    return render(request, "blog/article1.html")

def article2(request):
    return render(request, "blog/article1.html")

def article3(request):
    return render(request, "blog/article1.html")