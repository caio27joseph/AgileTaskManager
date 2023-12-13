from django.forms.models import model_to_dict
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Setting the owner to the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        return Response(model_to_dict(project))

    def put(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(model_to_dict(project))
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        project.delete()
        return HttpResponse(status=204)


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Setting the owner to the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        task = self.get_object(pk)
        if task is None:
            return HttpResponse(status=404)
        return Response(model_to_dict(task))

    def put(self, request, pk, *args, **kwargs):
        task = self.get_object(pk)
        if task is None:
            return HttpResponse(status=404)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(model_to_dict(task))
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        task = self.get_object(pk)
        if task is None:
            return HttpResponse(status=404)
        task.delete()
        return HttpResponse(status=204)
