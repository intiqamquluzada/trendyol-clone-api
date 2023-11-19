from django.urls import path
from accounts.views import *

app_name = 'accounts'
urlpatterns = [

    path("login/", LoginView.as_view(), name='login'),
    path("register/", RegisterView.as_view(), name='register'),
    path("logout/", logout_view, name="logout"),
    path("verify/", VerifyAPI.as_view(), name="verify"),


]
