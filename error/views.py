from django.shortcuts import render

# Create your views here.
def custom_404(request, exception):
    return render(request, 'error/404.html', status=404)


def custom_500(request):
    return render(request, 'error/500.html', status=500)