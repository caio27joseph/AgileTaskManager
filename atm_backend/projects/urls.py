from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateDeleteView,
    TaskListCreateView,
    TaskRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("projects/", ProjectListCreateView.as_view(), name="project_list_create"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDeleteView.as_view(),
        name="project_retrieve_update_delete",
    ),
    path("tasks/", TaskListCreateView.as_view(), name="task_list_create"),
    path(
        "tasks/<int:pk>/",
        TaskRetrieveUpdateDeleteView.as_view(),
        name="task_retrieve_update_delete",
    ),
]
