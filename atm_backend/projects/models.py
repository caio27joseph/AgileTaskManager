from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="projects", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)  # e.g., "New", "In Progress", "Completed"
    assigned_to = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, related_name="assigned_tasks"
    )
    due_date = models.DateField(null=True, blank=True)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title
