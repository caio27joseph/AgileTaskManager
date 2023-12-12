from django.http import HttpResponse
from .models import Project

from rest_framework.response import Response
from .forms import ProjectForm
import json
from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class ProjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all().values()
        return Response(list(projects))

    def post(self, request, *args, **kwargs):
        data = json.loads(request.data)
        form = ProjectForm(data)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner_id = request.user.id
            project.save()
            return Response(model_to_dict(project), status=201)
        return Response(form.errors, status=400)


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
        data = json.loads(request.body)
        form = ProjectForm(data, instance=project)
        if form.is_valid():
            project = form.save()
            return Response(model_to_dict(project))
        return Response(form.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        project.delete()
        return HttpResponse(status=204)
