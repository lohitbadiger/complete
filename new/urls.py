from django.urls import path

from . import views 
urlpatterns = [

    path('', views.home, name="new-home"),
    path('about', views.about, name="new-about"),
    path('contact', views.contact, name="new-contact"),

]
