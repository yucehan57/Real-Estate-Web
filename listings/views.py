from django.shortcuts import render
from .models import Listing

def index(request):
    """Main index page for all listings"""
    listings = Listing.objects.all() #Fetch all Listing objects from database

    context = {
        'listings': listings,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """Single Listing page"""
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    """Search page"""
    return render(request, 'listings/search.html')
