from django.conf.urls import url
from admin.housing import views

urlpatterns = {
    url(r'housing_info', views.housing_info)
}