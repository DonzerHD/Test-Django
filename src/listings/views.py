from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band,Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})
def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing_details.html', {'listing': listing})

def contact_us(request):
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    if request.method == 'POST':
            # créer une instance de notre formulaire et le remplir avec les données POST
            form = ContactUsForm(request.POST)

            if form.is_valid():
                send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )

        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                'listings/contact_us.html',
                {'form': form})
