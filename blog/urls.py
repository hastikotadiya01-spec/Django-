from django.urls import path 
from . import views  

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    path('blogpost/<slug:slug>/', views.blogPost, name="blogPost"), 
]