from django.conf.urls import url

from admin.nlp import views

urlpatterns = {
    url(r'HomonymClassification', views.HomonymClassification),
    url(r'naver_process', views.naver_process)
}