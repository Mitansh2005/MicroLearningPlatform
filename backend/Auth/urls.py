from django.urls import path
from Auth.views import (
    UserRegisteration,
    UserLogin,
    UserProfileView,
    ChangeUserPassword,
)

urlpatterns = [
    path("register/", UserRegisteration.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("Userprofile/", UserProfileView.as_view(), name="profile"),
    path("changepassword/", ChangeUserPassword.as_view(), name="change_password"),
]
