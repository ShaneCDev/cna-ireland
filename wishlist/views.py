from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Wishlist, WishlistItem
from django.contrib import messages
from products.models import Product
from urllib.parse import urlparse


# Create your views here.
def wishlist(request):
    wishlist = Wishlist.objects.filter(owner=request.user).first()
    wishlist_items = wishlist.wishlist.all() if wishlist else None
    context = {
        'wishlist_items': wishlist_items
    }
    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Sorry only verified in users can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=id)
    previous_page = request.META.get('HTTP_REFERER')
    previous_page_parsed = urlparse(previous_page or '')
    product_detail_path = f'/products/{product.slug}'

    try:
        wishlist_already_exists = Wishlist.objects.get(owner=request.user)
    except Wishlist.DoesNotExist:
        wishlist_already_exists = Wishlist.objects.create(owner=request.user)

    if wishlist_already_exists:
        wishlist_item = WishlistItem.objects.filter(product=product, wishlist=wishlist_already_exists).first()

        if not wishlist_item:
            wishlist_item = WishlistItem.objects.create(product=product)
            wishlist_already_exists.wishlist.add(wishlist_item)
            messages.success(request, "Item added to your wishlist!")
        else:
            messages.error(request, "Item is already on your wishlist.")
    else:
        wishlist = Wishlist.objects.create(owner=request.user)
        if not wishlist_item:
            wishlist_item = WishlistItem.objects.create(product=product)
            wishlist.wishlist.add(wishlist_item)
            wishlist.save()
            messages.success(request, "Item added to your wishlist!")
        else:
            messages.error(request, "Item is already on your wishlist.")
    if previous_page_parsed.path == product_detail_path:
        return redirect(reverse('product_detail', kwargs={'slug': wishlist_item.product.slug}))
    else:
        return redirect(reverse('products'))
    

def remove_from_wishlist(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Sorry only verified in users can do that.")
        return redirect(reverse('home'))
    product = get_object_or_404(Product, id=id)

    wishlist = Wishlist.objects.get(owner=request.user)

    wishlist_items = WishlistItem.objects.filter(product=product, wishlist=wishlist)

    if wishlist_items.exists():
        for item in wishlist_items:
            item.delete()
        messages.success(request, "Item removed from your wishlist.")
        return redirect('wishlist')

    
    






