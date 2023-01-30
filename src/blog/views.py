from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")
     
def article(request, numero_article):
    if numero_article in [1 , 2]:
        return render(request, f"blog/article{numero_article}.html")
    return render(request, f"blog/article_no_found.html")
