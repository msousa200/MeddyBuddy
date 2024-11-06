from django.urls import path
from .views import user_login, user_logout, register, profile

app_name = "users"

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
