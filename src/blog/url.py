from django.urls import path
from .views import index,article


urlpatterns = [
    path('',index, name="blog-index"),
    path('article<int:numero_article>/',article, name="article"),
]