from django.urls import path
from .views import index,article1,article2,article3


urlpatterns = [
    path('',index, name="blog-index"),
    path('article1',article1, name="article1"),
    path('article2',article2, name="article2"),
    path('article3',article3, name="article3"),
]