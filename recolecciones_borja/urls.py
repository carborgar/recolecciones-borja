"""recolecciones_borja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    # Auth URLS
    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name="logout"),
    # Welcome url is login page
    url(r'^$', RedirectView.as_view(pattern_name='login', permanent=False)),
    # Applications menu page
    url(r'^menu/', TemplateView.as_view(template_name='index.html')),
    # Invoices app urls
    url(r'^invoices/', include('invoices.urls')),
    # Customers app urls
    url(r'^customers/', include('customers.urls')),
    # Admin site urls
    url(r'^admin/', admin.site.urls),
]
