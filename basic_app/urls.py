from basic_app import views
# from django.urls import re_path
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special'),
]