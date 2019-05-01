from django.urls import path
from . import views

app_name = 'bookcrud'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-book/', views.create_book, name='create-book'),
    path('(?P<pk>\d+)/update/', views.update_book, name='update-book'),
    path('(?P<pk>\d+)/delete/', views.delete_book, name='delete-book'),
]
