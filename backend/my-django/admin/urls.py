from django.conf.urls import url

from admin.user import views

urlpatterns = {
    url(r'^api/register', views.users),
    url(r'^api/list', views.users)
}
