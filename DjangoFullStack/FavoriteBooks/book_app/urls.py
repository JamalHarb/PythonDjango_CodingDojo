from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('/add_book', views.add_book),
    path('/add_favorite/<int:id>/main', views.add_favorite_main),
    path('/add_favorite/<int:id>', views.add_favorite),
    path('/<int:id>', views.show_book),
    path('/modify/<int:id>', views.modify_book),
    path('/<int:id>/unfavorite', views.unfavorite),
]