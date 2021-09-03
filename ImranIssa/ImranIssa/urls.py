"""ImranIssa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Customer import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('packages/',views.packages,name='packages'),
    path('package_detail/<str:pk>/',views.package_detail,name='package_detail'),
    path('customer_detail/',views.customer_detail,name='customer_detail'),
    path('customer_detail/<str:pk>/',views.customer_detail_pk,name='customer_detail_pk'),
    path('detail/',views.detail,name='details'),

   

]
