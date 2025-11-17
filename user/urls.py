from django.urls import path
from user.views import CreateUserView, LoginUserView, ManageUserView
from rest_framework.authtoken import views

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="get_token"),
    path("me/", ManageUserView.as_view(), name="me"),
]
app_name = "user"
