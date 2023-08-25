from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    template = 'blog/blogs.html'

    return render(request, template, context)

