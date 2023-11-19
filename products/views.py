from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Category, Product, ProductReview
from .forms import ProductForm, CategoryForm, ReviewForm
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    """Show all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
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
                messages.error(request, "You didn't enter any search criteria!")
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
    all_reviews = ProductReview.objects.filter(product=product)
    paginator = Paginator(all_reviews, 3)
    page = request.GET.get('page')

    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)


    if request.user.is_anonymous:
        context = {
            'product': product,
            'all_reviews': all_reviews,
            'reviews': reviews
        }
    else:
        already_reviewed = all_reviews.filter(author=request.user)
        if already_reviewed:
            reviewed = True
        else:
            reviewed = False
        context = {
            'product': product,
            'all_reviews': all_reviews,
            'reviewed': reviewed,
            'reviews': reviews,
        }

    return render(request, 'products/product_detail.html', context)


def review(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, initial={'author': request.user})
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect(reverse('product_detail', kwargs={'slug': product.slug}))
    else:
        form = ReviewForm(initial={'author': request.user})
    
    template = 'products/product_review.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def add_product(request):
    """add a product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', kwargs={'slug': product.slug}))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_category(request):
    """Add categories"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, 'Category added successfully!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add Category, please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'products/add_category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, slug, product_id):
    """Edit products"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product edited successfully.')
            return redirect(reverse('product_detail', args=[slug]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing { product.name }')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, id):
    """delete products from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, f'{ product.name } deleted.')
    return redirect(reverse('products'))


@login_required
def edit_review(request, slug, id):
    product = get_object_or_404(Product, slug=slug)
    review = get_object_or_404(ProductReview, id=id)

    if request.user != review.author:
        print(request)
        messages.error(request, 'Sorry you can not do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review successfully edited!')
            return redirect(reverse('product_detail', kwargs={'slug': product.slug}))
    form = ReviewForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'products/edit_review.html', context)


@login_required
def delete_review(request, id):
    review = get_object_or_404(ProductReview, id=id)
    if request.user != review.author:
        messages.error(request, 'Sorry you can not do that.')
        return redirect(reverse('home'))
    
    review.delete()
    messages.success(request, 'Your review was successfully deleted.')
    return redirect(reverse('product_detail', kwargs={'slug': review.product.slug}))
    
