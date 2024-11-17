from  django.urls import path
from . import views

urlpatterns = [
    path('', views.registerlogin, name="registerlogin"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"), 
    path('login/register', views.register, name='register'), # From Login -> Register.
    path('home/', views.home, name="home"),
]
