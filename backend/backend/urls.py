"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
# TokenObtainPairView, TokenRefreshView are an pre-build tools which allows us to obtain access and refresh token into refresh the token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# This file is for the URL configuration of the project. It is the main entry point of the project.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),  # will provide the access token
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),  # will provide the refresh token
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),  # Include the urls of the api app in the project urls file so that we can access the api routes from the project urls file itself
]
