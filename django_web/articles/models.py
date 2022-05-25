from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.CharField(max_length = 200)
    title = models.CharField(max_length=250, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time update')
    is_published = models.BooleanField(verbose_name='Is Published', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-time_create']


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Category name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


    def __str__(self):
        return self.name


# class SetupAccount(models.Model):
#     account_photo = models.ImageField(upload_to='account_photo/%Y/%m/%d', verdose_name='Account photo')
#     biography = models.TextField(verbose_name='Biography')
#     status = models.CharField(max_length=100, verbose_name='Status')
    
