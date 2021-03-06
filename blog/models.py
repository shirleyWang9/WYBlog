from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    class Meta:
        verbose_name = _('博客')
        verbose_name_plural = _('博客')

    title = models.CharField(max_length=100, unique=True, verbose_name=_('标题'), help_text='博客的标题')
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, null=True)
    author = models.ForeignKey(User, verbose_name=_('作者'), on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('URL'))
    body = RichTextUploadingField(verbose_name=_('正文'))
    posted = models.DateField(db_index=True, auto_now_add=True)


    def __str__(self):
        return '%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return 'blog_view', None, {'slug': self.slug}

