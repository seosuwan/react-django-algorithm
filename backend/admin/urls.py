"""admin URL Configuration
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
from django.urls import path, include
from django.conf.urls import url

from admin.user import views

urlpatterns = [
    path('api/connect', include('admin.common.urls')),
    path('api/housing/', include('admin.housing.urls')),
    path('api/users/', include('admin.user.urls')),
    path('api/crime/', include('admin.crime.urls')),
    path('api/crawling/', include('admin.crawling.urls')),
    path('api/tensor/', include('admin.tensor.urls')),
    path('api/iris/', include('admin.iris.urls')),
    path('api/myCV2/', include('admin.myCV2.urls')),
    path('api/rnn/', include('admin.rnn.urls')),
    path('api/aiTrader/', include('admin.aiTrader.urls')),
    path('api/nlp/', include('admin.nlp.urls')),
    path('api/myGAN/', include('admin.myGAN.urls')),
]
