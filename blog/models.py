from django.db import models
from django.db.models import permalink
from django.utils import timezone

class Blog(models.Model):
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=260, unique=True, blank=True)
    image = models.CharField(max_length=260, unique=False, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    posted_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image_ind = models.CharField(max_length=260, unique=True, blank=True)
    image_cat = models.CharField(max_length=260, unique=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Home(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    body=models.TextField()

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_home', None, { 'slug': self.slug })
