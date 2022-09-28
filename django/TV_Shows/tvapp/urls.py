from django.urls import path
from . import views


urlpatterns = [
    path('',views.root),
    path('shows',views.index),
    path('shows/new',views.new_show),
    path('shows/create',views.add_show),
    path('shows/<int:showid>',views.show),
    path('shows/<int:showid>/edit',views.edit_show),
    path('update_show_info',views.update_show),
    path('shows/<int:showid>/delete',views.delete_show)
]