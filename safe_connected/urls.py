from django.contrib import admin
from django.urls import path, include
from safe_connected import views


urlpatterns = [
    # POST
    path("event/create/", views.EventViewSet.as_view(), name="create-event"),
    path("event/list/", views.EventListViewSet.as_view(), name="list-event"),
    path("event/search/", views.EventSearchViewSet.as_view(), name="event_search"),
    path("event/roster/", views.EventRosterViewSet.as_view(), name="event-roster"),
    path("event/roster/create/", views.EventRosterCreateViewSet.as_view(),
         name="event-roster-create"),
]
