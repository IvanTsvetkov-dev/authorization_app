from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("registration/", views.registration_user, name="registration"),
    path("logout/", views.logout_user, name="logout")
]
