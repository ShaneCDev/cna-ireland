from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    template = 'blog/blogs.html'

    return render(request, template, context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'blog': blog,
    }
    template = 'blog/blog_detail.html'
    return render(request, template, context)