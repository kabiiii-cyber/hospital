
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index,name='home'),
    path('service/', views.services,name='service'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('departments/', views.departments,name='departments'),
    path('doctors/', views.doctors,name='doctors')

]
