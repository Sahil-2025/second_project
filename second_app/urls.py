from django.urls import path

from second_app import views

app_name = "second_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_list/', views.user_list, name='user_list'),
]