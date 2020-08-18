from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request, 'all_blogs.html', {'blogs' : blogs})

def detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    return render(request, 'detail.html', {'blog':blog})
