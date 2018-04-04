from django.conf.urls import url
from blog.views import blog_detail


urlpatterns = [
    url(r'^(?P<slug>[^\.]+).html', blog_detail, name='blog_view'),
]
