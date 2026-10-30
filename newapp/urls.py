from django.urls import path

from newapp import views

urlpatterns = [
    path("",views.home,name="home"),
]
