from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from . import models


def homeview(request):
    data = {
        "project": models.Project.objects.all(),
    }
    
    return render(request, "home.html", data)


def view_project(request, project_id):
    project = get_object_or_404(models.Project, id=project_id)
    data = {
        "project": project,
    }

    return render(request, "projects.html", data)
