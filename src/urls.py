from apps.core.views import index
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", index, name="index"),
    path("pongellupi/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += (path("__reload__/", include("django_browser_reload.urls")),)
