from django.conf.urls import url

from . import views

app_name = 'juice'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/add_member/$', views.add_member, name='add_member'),
    url(r'^/login/$', views.login, name='login'),
    url(r'^/login_check/$', views.login_check, name='login_check'),
]