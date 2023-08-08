from apps.core.views import index
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", index, name="index"),
    path("pongellupi/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
