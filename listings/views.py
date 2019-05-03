from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    """Main index page for all listings that are published.
       Paginated by 3 listings a page"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6) # Show listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'listings': paged_listings
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
