from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from .models import *
from .forms import *


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, 'articles/about.html')


def contact(request):
    return render(request, 'articles/contact.html')


def your_articles(request):
    return render(request, 'articles/your_articles.html')


# def write_article(request):
#     return render(request, 'articles/write_article.html')



def profile(request):
    return render(request, 'articles/profile.html')

def show_articles(request):
    posts = Article.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'articles/show_articles.html', context)


class WriteArticle(FormView):
    form_class = WriteArticleForm
    template_name = 'articles/write_article.html'
    success_url = reverse_lazy('your_articles')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
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