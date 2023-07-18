from django.contrib import admin
from django.urls import path, include
from safe_connected import views


urlpatterns = [
    # POST
    path("event/create/", views.EventViewSet.as_view(), name="create-event"),
]