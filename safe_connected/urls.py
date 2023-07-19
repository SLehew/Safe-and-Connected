from django.contrib import admin
from django.urls import path, include
from safe_connected import views


urlpatterns = [
    # POST
    path("event/create/", views.EventViewSet.as_view(), name="create-event"),
    # GET
    path("event/list/", views.EventListViewSet.as_view(), name="list-event"),
    # GET
    path("event/search/", views.EventSearchViewSet.as_view(), name="event-search"),
    # GET|UPDATE|DESTROY
    path("event/roster/<int:pk>", views.EventRosterViewSet.as_view(), name="event-roster"),
    path("event/roster/create/", views.EventRosterCreateViewSet.as_view(),
         name="event-roster-create"),
    path("organization/create/",
         views.OrganizationProfileViewSet.as_view(), name="create-org"),
    path("organization/",
         views.OrganizationProfileViewSet.as_view(), name="org-list"),
    path("organization/<int:pk>/",
         views.EditOrganizationProfileViewSet.as_view(), name="org-detail"),
    path("organization/edit/<int:pk>/",
         views.EditOrganizationProfileViewSet.as_view(), name="org-edit"),
]
