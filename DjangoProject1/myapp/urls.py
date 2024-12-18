
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('doors/', views.doors, name='doors'),
    path('doors/<int:door_id>/', views.door_detail, name='door_detail'),
    path('search/<str:query>/', views.search_doors, name='search_doors'),
]