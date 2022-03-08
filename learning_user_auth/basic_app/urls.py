from basic_app import views
from django.urls import re_path

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^register/$', views.register, name='registration'),
    re_path(r'^user_login/$', views.user_login, name='user_login'),
    re_path(r'^user_logout/$', views.user_logout, name='user_logout'),
    re_path(r'^special/$', views.special, name='special'),
]