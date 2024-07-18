from django.shortcuts import render , redirect
from django.contrib.auth import logout
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return(redirect("/"))

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter