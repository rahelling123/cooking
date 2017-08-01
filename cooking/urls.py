"""cooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from usermanage.views import index, login_custom, signup_customer, logout_custom, dashboard, signup_restaurant, dashboard_restaurant
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^signup_restaurant/$', signup_restaurant, name='signup_restaurant'),
    url(r'^signup_customer/$', signup_customer, name='signup_customer'),
    url(r'^dashboar_restaurant/$', dashboard_restaurant, name='dashboard_restaurant'),
    url(r'^login/$', login_custom, name='login'),
    url(r'^logout/$', logout_custom, name='logout'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
