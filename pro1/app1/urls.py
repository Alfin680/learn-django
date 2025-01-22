from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('register/',views.register,name = 'register'),
    path('registerdetails/',views.regDetails, name = 'regdetails'),
    path('Login/',views.loginUser, name = 'loginUser'),
    path('Home/',views.home, name = 'Home'),
    path('Blog/',views.blog, name = 'blog'),
    path('BlogData/', views.blog_ , name= 'blogData'),
    path('BlogUpdate/<int:pk>/', views.blogUpdate , name= 'blogUpdate'),
    path('BlogUpdate/update/<int:pk>', views.update , name= 'blogUpdate_')
]
