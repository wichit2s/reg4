"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from api.urls import router as apirouter
from noteapp.views import note

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', note),


    path('admin/', admin.site.urls),
    path('api/', include(apirouter.urls)),

    path('auth/', include('djoser.urls')),

    path('restapi/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('restapi/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
