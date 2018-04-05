from django.conf.urls import url
from blog.views import blog_detail,blog_with_type


urlpatterns = [

    url(r'^(?P<slug>(?!-)(?!.*?-$)[0-9a-zA-Z]+(-)+[^\.]+).html', blog_detail, name='blog_view'),
    url(r'^type/(?P<blog_type_pk>[0-9]+).html', blog_with_type, name='blog_with_type'),

]
