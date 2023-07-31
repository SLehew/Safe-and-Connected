from django.contrib import admin
from django.urls import path, include
from safe_connected import views

urlpatterns = [
    # ----------EVENTS---------
    # POST | Create an Event
    path("event/create/", views.EventViewSet.as_view(), name="create-event"),
    # GET | List All Events Created by the Manager
    path("event/organizer/list/",
         views.EventListViewSet.as_view(), name="list-event"),
    # GET | List All Events for Clients Organizations in English
    path("client/event/list/", views.EventHomeClientViewSet.as_view(),
         name="client-list-event-"),
    # GET | List All Events for Clients Organizations in Spanish
    path("es/client/event/list/", views.EventHomeClientViewSet.as_view(),
         name="client-list-event-es"),
    # GET | List All Events for Clients Organizations in French
    path("fr/client/event/list/", views.EventHomeClientViewSet.as_view(),
         name="client-list-event-fr"),
    # GET | List All Events for Clients Organizations in Swahili
    path("sw/client/event/list/", views.EventHomeClientViewSet.as_view(),
         name="client-list-event-sw"),
    # GET | Event Details in English
    path("event/<int:pk>/details/",
         views.EventDetailViewSet.as_view(), name="event-detail"),
    # GET | Event Details in Spanish
    path("d2e07b2de5073f9540960eeb0b8a7f2d687ac244",
         views.EventDetailViewSet.as_view(), name="event-detail"),
    # GET | Event Details in French
    path("fr/event/<int:pk>/details/",
         views.EventDetailViewSet.as_view(), name="event-detail"),
    # GET | Event Details in Swahili
    path("sw/event/<int:pk>/details/",
         views.EventDetailViewSet.as_view(), name="event-detail"),
    # PATCH|UPDATE|DELETE | Manager Edit Event
    path("event/<int:pk>/details/",
         views.EventDetailViewSet.as_view(), name="event-detail"),
    # GET | List ALL Events
    path("event/all/", views.EventSearchViewSet.as_view(), name="event-all"),
    # GET | List All Organizations Events
    path("org/<int:event_organization_id>/events/",
         views.OrgEventListViewSet.as_view(), name="org_events"),
    # GET| add (/?event_title= or /?general_notes=) to url | Text Search Event Titles & Notes
    path("event/search/", views.EventSearchViewSet.as_view(), name="event-search"),
    # GET List of Clients Attending Event (pk is event_id)
    path("event/roster/<int:pk>/",
         views.EventRosterViewSet.as_view(), name="event-roster"),
    # PATCH | Client Sign Up for Event (pk is event_id)
    path("event/roster/<int:pk>/signup/",
         views.EventRosterUpdateViewSet.as_view(), name="event-roster"),
    # GET List of the Events Client is Attending
    path("event/client/", views.ClientEventAttending.as_view(),
         name="client-events-attending"),
    # POST | Create Organization Profile
    path("organization/create/",
         views.OrganizationProfileViewSet.as_view(), name="create-org"),
    # GET | List of All Organizations
    path("organization/",
         views.OrganizationProfileViewSet.as_view(), name="org-list"),
    # GET | Organization Profile
    path("organization/<int:pk>/",
         views.EditOrganizationProfileViewSet.as_view(), name="org-detail"),
    # GET|UPDATE|DELETE | Edit Organization profile
    path("organization/edit/<int:pk>/",
         views.EditOrganizationProfileViewSet.as_view(), name="org-edit"),
    # POST | Add Language
    path("language/add/", views.LanguageViewSet.as_view(), name="add-language"),
    # POST | Add Client to Org Membership
    path("org/client/mem/create/", views.OrganizationMembershipViewSet.as_view(),
         name="create-organiz-client-membership"),
    # POST | Upload File
    path("uploads/", views.UploadCreateView.as_view()),
    # GET | Get List of Client Files
    path("files/user/<int:pk>/", views.FileViewSet.as_view()),
    # GET | List of all Org Client is Member Of
    path("org/mem/",
         views.MembershipView.as_view(), name="my-memberships"),
    # GET and PATCH | View and edit User Role
    path("user/<int:pk>/", views.UserRoleView.as_view(), name="user_role"),
    # GET | List All Org Clients
    path("org/<int:organization_id>/clients/",
         views.ClientListView.as_view(), name="org-clients"),
    # POST | Upload User Avatar
    path("user/<int:pk>/image/",
         views.UploadUserAvatarView.as_view(), name="user-avatar"),
]
