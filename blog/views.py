from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import linebreaksbr


def all_blogs(request):
    blogs = Blog.objects.all()

    sorted_blogs = blogs.order_by('-blog_date')

    print(sorted_blogs)

    context = {
        'blogs': sorted_blogs,
    }
    template = 'blog/blogs.html'

    return render(request, template, context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    content_paragraphs = linebreaksbr(blog.content).split('<br>')

    content_paragraphs = [p.strip() for p in content_paragraphs if p.strip()]

    context = {
        'blog': blog,
        'content_paragraphs': content_paragraphs,
    }
    template = 'blog/blog_detail.html'
    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """delete a blog"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()

    # show_grand_total = False

    messages.success(request, 'Blog post deleted.')
    return redirect(reverse('blogs'))
