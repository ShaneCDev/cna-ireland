from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from .forms import ProductForm
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages


def all_products(request):
    """Show all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in  request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in  request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # add message
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """Detailed view of the product"""
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """add a product"""
    if not request.user.is_superuser:
        # add messages
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # add messages
            return redirect(reverse('product_detail'), args=[product.slug])
        else:
            # add messages
            print('add messages')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug, product_id):
    """Edit products"""
    if not request.user.is_superuser:
        # add messages later
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # add messages later
            return redirect(reverse('product_detail', args=[slug]))
        else:
            print('add messages later')
    else:
        form = ProductForm(instance=product)
        # add messages later
    
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """delete products from the store"""
    if not request.user.is_superuser:
        # add messages
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    # add messages
    return redirect(reverse('products'))