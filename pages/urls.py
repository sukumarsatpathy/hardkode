from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='service'),
    path('services/web-development', views.webDevlopment, name='web-development'),
    path('projects/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
]