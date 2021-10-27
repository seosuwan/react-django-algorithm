from django.conf.urls import url

from admin.myGAN import views

urlpatterns = {
    url(r'AutoencodersAndGans', views.AutoencodersAndGans),
}