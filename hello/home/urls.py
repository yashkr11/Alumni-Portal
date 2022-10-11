from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("index",views.index, name='index'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("register",views.register, name='register'),
    path("alumnistories", views.Alumni_Stories , name='alumnistories'),
    path("viewstory/<int:story_id>", views.ReadStory , name='viewstory'),
]
