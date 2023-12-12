from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDeleteView

urlpatterns = [
    path("", ProjectListCreateView.as_view(), name="project_list_create"),
    path(
        "<int:pk>/",
        ProjectRetrieveUpdateDeleteView.as_view(),
        name="project_retrieve_update_delete",
    ),
]
