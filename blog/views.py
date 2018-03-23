from django.shortcuts import render_to_response, get_object_or_404

from blog.models import Blog

from django.contrib.auth.models import User

# Create your views here.

def blog_list(request):
    return render_to_response('blog/list.html', {
        'blogs': Blog.objects.all()

    })

def blog_detail(request,slug):
    return render_to_response('blog/detail.html',{
        'blog': get_object_or_404(Blog, slug=slug)
    })

# def index(request):
#     return render_to_response('index.html', {
#         'blogs': Blog.objects.all()
#     })