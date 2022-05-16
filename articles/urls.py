from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('about/', views.about, name='about'),
    path('logout', views.logout_user, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('', views.show_articles, name='articles'),
    path('write_article/', views.WriteArticle.as_view(), name='write_article'),
    path('your_articles', views.your_articles, name='your_articles'),
    path('profile', views.profile, name='profile'),
    path('article/<int:article_id>', views.article, name='article'),
    path('category/<int:cat_id>', views.category, name='category')
]
