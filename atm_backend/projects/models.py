from django.conf import settings
from django.db import models

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
