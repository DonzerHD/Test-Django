from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band,Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

def contact_us(request):
    return render(request, 'listings/contact_us.html')
