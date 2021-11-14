from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import signup, user_logout

app_name = "accounts-v1"

urlpatterns = [
    path("api/v1/signup/", signup, name="signup"),
    path("api/v1/login/", obtain_auth_token, name="api-login-token"),
    path("api/v1/logout/", user_logout, name="logout"),
]
