from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('+2', views.plus_two),
    path('+num', views.plus_num)
]
