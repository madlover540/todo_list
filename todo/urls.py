from django import views
from django.urls import path
from todo import views



urlpatterns = [
    path('', views.index, name=('home')),
    path('<int:pk>/delete/', views.deletetask, name ='delete'),
    
]
