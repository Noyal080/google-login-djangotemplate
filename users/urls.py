from django.urls import path
from . import views
from .views import GoogleLogin

urlpatterns = [
    path("" ,views.home),
    path("logout" , views.logout_view),
    path('google/login/token', GoogleLogin.as_view() , name='google_login_token')
]