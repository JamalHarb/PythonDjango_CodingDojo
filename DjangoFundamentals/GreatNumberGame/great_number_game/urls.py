import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('handle_guess', views.handle_guess),
    path('right_guess', views.right_guess),
]