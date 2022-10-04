from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),#landing page/main page
    path('register',views.registeration),#registration method
    path('login',views.check),#checks log in information
    path('log_out',views.delete_session),#deletes user info from session and redirects to the root route
]