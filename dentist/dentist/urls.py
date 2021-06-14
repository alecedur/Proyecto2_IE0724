"""dentist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appointments import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('show/', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('signup/', views.signup, name = 'signup'),
    path('superuser/', views.superuser, name = 'superuser'),
    #path('login/', views.login, name = 'login'),
    path('login/user/view/', views.userView, name= 'userView'),
    path('user/delete/', views.userDelete, name= 'userDelete'),
    path('user/modify/', views.userModify, name='userModify'),
    path('login/admin/panel/', views.superuserView, name = 'superuserView'),

    #Django Auth Stuff
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout')
]
