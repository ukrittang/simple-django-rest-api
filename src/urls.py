from allauth.socialaccount.providers.facebook.views import \
    FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.contrib import admin
from django.urls import include, path
from rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/register/', include('rest_auth.registration.urls')),
    path('api/auth/google/', GoogleLogin.as_view()),
    path('api/auth/facebook/', FacebookLogin.as_view()),
    path('api/articles/', include('articles.urls')),
]
