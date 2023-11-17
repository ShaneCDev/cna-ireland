from django.shortcuts import render


def index(request):
    """Render the home page"""

    return render(request, 'home/index.html')


def terms_and_conditions(request):
    return render(request, 'home/terms.html')


def privacy(request):
    return render(request, 'home/privacy.html')
