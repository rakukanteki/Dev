from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('blogs/', views.blogs, name='blog'),
    # path('about/', views.about, name='aboutpage'),
    # path('about/radwan/', views.radwan, name='aboutpage'),
    # path('registration/', views.registration, name='Registration Form'),
    # # path('registration/counter/', views.counter, name='Word Counter'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
