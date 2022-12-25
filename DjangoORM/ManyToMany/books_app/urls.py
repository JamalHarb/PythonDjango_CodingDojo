from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books),
    path('add_book', views.add_book),
    path('books/<int:_id>', views.show_book),
    path('assign_author', views.assign_author),
    path('authors', views.all_authors),
    path('add_author', views.add_author),
    path('authors/<int:_id>', views.show_author),
    path('assign_book', views.assign_book),
]