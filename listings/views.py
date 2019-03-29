from django.shortcuts import render


def index(request):
    """Main index page for all listings"""
    return render(request, 'listings/listings.html')


def listing(request):
    """Single Listing page"""
    return render(request, 'listings/listing.html')


def search(request):
    """Search page"""
    return render(request, 'listings/search.html')
