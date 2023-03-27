from django.urls import path
from user.views import register_view
from django.contrib.auth import views

urlpatterns= [
    path('register/', register_view, name='register'),
    path('login/', views.LoginView.as_view(template_name="user/login.html"), name="user_login")
]