from products.models import Category


def category_nav(request):
    categories = list(Category.objects.all())
    return {'categories': categories}