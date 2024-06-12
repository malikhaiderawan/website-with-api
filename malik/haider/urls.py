from django.contrib import admin
from django.urls import path

from haider import views


urlpatterns = [
    path('',views.index, name='haider'),
    path('details',views.details, name='details'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('feedback',views.feedback, name='feedback'),
    path('home',views.home, name='home'),
    #contactapi
    path('contactapi',views.contact_api),
    path('contactapi/<int:id>', views.contact_detail),
    #feedback api
    path('feedbackapi',views.Feedback_api),
    path('feedbackapi/<int:id>',views.Feedback_detail),
    #Home api
    path('homeapi',views.Home_api),
    path('homeapi/<int:id>',views.Home_detail),




]
