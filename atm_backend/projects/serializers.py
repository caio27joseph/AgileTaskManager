from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "end_date"]
        # Note: 'owner' is excluded, similar to your form

    def validate(self, data):
        """
        Check that the end date is not before the start date.
        """
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        if end_date and start_date and end_date < start_date:
            raise serializers.ValidationError("End date cannot be before start date.")
        return data


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), required=False
    )
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "assigned_to", "due_date", "project"]
