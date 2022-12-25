from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_form),
    path('results', views.show_results),
]