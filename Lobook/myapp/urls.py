from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('list', views.list, name='list'),
    path('login', views.login, name='login'),
    path('update', views.update, name='update'),
    path('lend', views.lend, name='lend'),
    path('delete', views.delete, name='delete'),
]