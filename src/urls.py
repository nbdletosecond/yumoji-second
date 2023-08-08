from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pongellupi/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
