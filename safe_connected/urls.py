from django.contrib import admin
from django.urls import path, include
from safe_connected import views


urlpatterns = [
    # POST
    path("event/create/", views.EventViewSet.as_view(), name="create-event"),
    # GET
    path("event/list/", views.EventListViewSet.as_view(), name="list-event"),
    # GET
    path("Client/event/list/", views.EventHomeClientViewSet.as_view(),
         name="client-list-event"),
    # GET|UPDATE|DELETE
    path("event/<int:pk>/details/",
         views.EventDetailViewSet.as_view(), name="event-detail"),
    # GET
    path("event/search/", views.EventSearchViewSet.as_view(), name="event-search"),
    # GET|UPDATE|DESTROY
    path("event/roster/<int:pk>",
         views.EventRosterViewSet.as_view(), name="event-roster"),
    # POST
    path("event/roster/create/", views.EventRosterCreateViewSet.as_view(),
         name="event-roster-create"),
    # POST
    path("organization/create/",
         views.OrganizationProfileViewSet.as_view(), name="create-org"),
    # GET
    path("organization/",
         views.OrganizationProfileViewSet.as_view(), name="org-list"),
    # GET
    path("organization/<int:pk>/",
         views.EditOrganizationProfileViewSet.as_view(), name="org-detail"),
    # GET|UPDATE|DELETE
    path("organization/edit/<int:pk>/",
         views.EditOrganizationProfileViewSet.as_view(), name="org-edit"),
    # POST
    path("language/add/", views.LanguageViewSet.as_view(), name="add-language"),
    # POST
    path("org/client/mem/create/", views.OrganizationMembershipViewSet.as_view(),
         name="create-organiz-client-membership"),
    path("org/client/mem/", views.OrganizationMembershipViewSet.as_view(),
         name="create-organiz-client-membership"),
    # POST
    path("uploads/", views.UploadCreateView.as_view()),

]
