from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.display_shows),
    path('shows/new', views.add_show),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.show_info),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/update', views.update_show),
    path('shows/<int:id>/delete', views.delete_show)
]