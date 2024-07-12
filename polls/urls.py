from django.urls import path

from . import views
# This is URL
urlpatterns = [
    path("", views.index, name="index"),
]