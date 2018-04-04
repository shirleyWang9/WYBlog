from django.contrib import admin

from blog.models import Blog, BlogType

admin.site.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

admin.site.register(Blog)

# Register your models here.
