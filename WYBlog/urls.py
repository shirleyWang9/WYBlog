"""WYBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from blog.api import BlogSet
from django.urls import include

from blog.views import blog_detail,blog_list

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blog', BlogSet)


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',blog_list),
    url(r'^blog/(?P<slug>[^\.]+).html', blog_detail, name='blog_view'),
    url(r'^api/',include(apiRouter.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)