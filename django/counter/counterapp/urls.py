from django.urls import path
from . import views
# Create your views here.
urlpatterns = [
    path('',views.index),  
    path('destroy_session',views.destroy_session),
    path('plus2',views.increase_counter_by_two),
    path('useradd',views.increase_counter_by_fixed_number)
]