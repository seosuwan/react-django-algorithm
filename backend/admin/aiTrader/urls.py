from django.conf.urls import url

from admin.aiTrader import views

urlpatterns = {
    url(r'process', views.process),

}
