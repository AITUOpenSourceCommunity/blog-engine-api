from django.urls import path

from .views import redirect


urlpatterns = [
    path("redirect/", redirect)
]
