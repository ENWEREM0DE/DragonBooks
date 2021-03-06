"""dragonBooksSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from dragonBooks import views
from django.contrib.auth import views as auth_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    path('codeSearch/', views.codeSearch, name='codeSearch'),
    path('<int:id>/', views.single, name='single'),
    path('searchCode/', views.searchCode, name='searchCode'),
    path('checkout/', views.checkout, name="checkout"),
    path('forthepress/', views.forthepress, name="forthepress"),
    path('booksellers/', views.booksellers, name="booksellers"),
    path('mediamentions/', views.mediamentions, name="mediamentions"),
    path('update_item/', views.updateItem, name="update_item"),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(
        template_name='dragonBooks/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(
        template_name='dragonBooks/logout.html'), name='logout'),
    path('profile/', views.profile, name="profile")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
