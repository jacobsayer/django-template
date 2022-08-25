from django.conf import settings
from django.contrib import admin
from django.urls import (
    include,
    path,
)
from rest_framework import routers

from accounts import views

router = routers.DefaultRouter()
router.register(r"users", views.CustomUserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
