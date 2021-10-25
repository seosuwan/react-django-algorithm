from django.conf.urls import url

from admin.nlp import views

urlpatterns = {
    url(r'Imdb_process', views.Imdb_process),
    url(r'naver_process', views.naver_process)
}