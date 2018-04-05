from django.shortcuts import render_to_response, get_object_or_404

from blog.models import Blog,BlogType

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

def blog_with_type(request,blog_type_pk):

    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    return render_to_response('blog/blog_with_type.html',{
        'blogs': Blog.objects.filter(blog_type=blog_type),
        'blog_type': blog_type

    })

# def index(request):
#     return render_to_response('index.html', {
#         'blogs': Blog.objects.all()
#     })