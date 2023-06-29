from django.urls import path

from . import views

urlpatterns = [
    path("profile/", views.CreateProfileView.as_view(), name="createprofile"),
    path("all_profiles/",views.AllProfilesView.as_view(),name="all_profiles")
]
