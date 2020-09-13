from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='registerForm'),
    path('login/', views.login_, name='loginForm'),
    path('logout/', views.logout_, name='logout_'),
]