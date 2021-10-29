from django.conf.urls import url
from admin.user import views

urlpatterns = {
    url(r'^join', views.users),
    url(r'^login', views.login),
    url(r'^detail/(?P<username>\w{0,50})/$', views.detail),
    url(r'^list', views.list),
    url(r'^modify', views.users),
    # url(r'^detail', views.detail),거지같은게 왜 또 여기 있냐 파라미터있으면 슬래시...줘야되낟...

}

'''
CBV 방식 (Class Based View)
from django.conf.urls import url
from .views import Members as members
from .views import Member as member
from django.urls import path, include
urlpatterns = [
    url('/register', members.as_view()),
    path('/<int:pk>/', member.as_view()),
]
'''