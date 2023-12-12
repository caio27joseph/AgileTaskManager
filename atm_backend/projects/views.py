from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Project
from .forms import ProjectForm
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class ProjectListCreateView(View):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all().values()
        return JsonResponse(list(projects), safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        form = ProjectForm(data)
        if form.is_valid():
            project = form.save()
            return JsonResponse(model_to_dict(project), status=201)
        return JsonResponse(form.errors, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class ProjectRetrieveUpdateDeleteView(View):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        return JsonResponse(model_to_dict(project))

    def put(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        data = json.loads(request.body)
        form = ProjectForm(data, instance=project)
        if form.is_valid():
            project = form.save()
            return JsonResponse(model_to_dict(project))
        return JsonResponse(form.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        project.delete()
        return HttpResponse(status=204)
