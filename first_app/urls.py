from django.urls import path

from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('help/', views.help),
    path('image/',views.image),
    path('webpages/',views.webpages),
    path('users/',views.users),
    path('form_name/',views.form_name),
    path('new_user/',views.new_user_form),
    path('page_one/',views.page_one),
    path('other/',views.other),
    path('other_five/',views.other_five),
    path('new_page/',views.new_page),
    path('other_three/',views.other_three, name='other_three'),
    path('other_four/',views.other_four, name='other_four'),
    path('base/',views.base),
    path('base_other/',views.base_other, name='base_other'),
    path('home/',views.home, name='home'),
    path('template_home/',views.template_home, name='template_home'),
    path('template_users/',views.template_users, name='template_users'),
    path('template_form/',views.template_form, name='template_form'),
]