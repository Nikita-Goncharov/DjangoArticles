from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('about/', views.about, name='about'),
    path('logout', views.logout_user, name='logout'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('', views.show_articles, name='articles'),
    path('write_article/', views.WriteArticle.as_view(), name='write_article'),
    path('your_articles', views.your_articles, name='your_articles'),
    path('profile', views.profile, name='profile'),
    path('article/<int:article_id>', views.article, name='article'),
    path('category/<int:cat_id>', views.category, name='category'),
    path('delete/<int:del_id>', views.delete_article, name='delete'),
    path('update/<int:pk>', views.UpdateArticle.as_view(), name='update'),
    path('profile-<str:user_name>', views.others_profile, name='others_profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='articles/password_reset.html'), name='reset_password'),
    path('password_reset_email/', auth_views.PasswordResetDoneView.as_view(template_name='articles/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="articles/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='articles/password_reset_complete.html'), name='password_reset_complete'),    
]
