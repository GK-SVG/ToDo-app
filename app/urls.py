from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('create-work',views.createdata,name='CreateData'),
    path('getData/',views.getdata,name='GetData'),
    path('delete/<int:id>',views.deletedata,name='DeleteData'),
    path('search/',views.search,name='search'),
    path('',views.index,name='Home'),   
]
