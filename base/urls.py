from django.urls import path 
from . import views 

urlpatterns=[ 
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),

    path('',views.home,name='home'),
    path('<str:pk>',views.profile,name='profile'),
    path('create-post/',views.createPost,name='create-post'),

]