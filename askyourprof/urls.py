"""askyourprof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from melon import views as melon_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', melon_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/sign-in.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('student/', melon_views.studpage, name='studpage'),
    path('professor/', melon_views.profpage, name='profpage'),
    path('student/<str:uname>', melon_views.view_prof, name='view_prof'),
    path('student/#/subscribe', melon_views.subscribe_view, name='subscribe_view'),
    path('professor/busy', melon_views.press_busy, name="busy"),
    path('professor/available', melon_views.press_available, name="available"),
]
