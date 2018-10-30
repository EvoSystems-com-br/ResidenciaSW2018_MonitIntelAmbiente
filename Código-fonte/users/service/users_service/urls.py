from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^cameras/$', views.CameraList.as_view(), name='camera-list'),
    url(r'^cameras/(?P<pk>[a-zA-Z0-9]+)/$', views.CameraDetail.as_view(), name='camera-detail'),
]
