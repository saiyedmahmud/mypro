from django.contrib import admin
from django.urls import path,include
from attendance import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('attendance',views.attendance, name='attendance'),
    path('studentinfo', views.studentinfo, name='studnetinfo'),
    path('login',views.userlogin, name='userlogin'),
    path('logout', views.userlogout, name='logout')

]
