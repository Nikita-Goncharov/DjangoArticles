from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, 'articles/about.html')


def article(request, article_id):
    artic = Article.objects.get(pk=article_id)
    context = {
        'artic': artic,
    }
    return render(request, 'articles/read_article.html', context)


def contact(request):
    return render(request, 'articles/contact.html')


@login_required
def your_articles(request):
    artic = Article.objects.filter(user=request.user.username)
    context = {
        'artic': artic,
    }
    return render(request, 'articles/your_articles.html', context)


def pageNotFound(request, exception):
    return render(request, 'articles/404.html')

@login_required
def profile(request):
    return render(request, 'articles/profile.html')


def show_articles(request):
    posts = Article.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'articles/show_articles.html', context)


def category(request, cat_id):
    cat_posts = Article.objects.filter(category=cat_id)
    cat = Category.objects.get(pk=cat_id)
    cats = Category.objects.all()
    context = {
        'cat_posts': cat_posts,
        'cat': cat,
        'cats': cats
    }
    return render(request, 'articles/category.html', context)

class WriteArticle(LoginRequiredMixin, FormView):
    form_class = WriteArticleForm
    template_name = 'articles/write_article.html'
    success_url = reverse_lazy('your_articles')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user.username
        f.save()
        return redirect(self.success_url)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'articles/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('articles')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'articles/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def get_success_url(self):
        return reverse_lazy('articles')