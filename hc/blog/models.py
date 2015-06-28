from django.db import models
from django.core.urlresolvers import reverse
from redactor.fields import RedactorField

class About(models.Model):
    content = RedactorField(verbose_name=u'Text')

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog.views.tag",args=[self.slug])

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,
                            max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255,default="Honestly Curated")
    content = RedactorField(verbose_name=u'Text')
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="posts", related_query_name="post", blank=True)
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        return reverse('blog.views.post',args=[self.slug])
