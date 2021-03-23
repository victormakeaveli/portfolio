from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from . import models


def indexview(request):
    data = {
        "project": models.Project.objects.all(),
    }
    
    return render(request, "index.html", data)

# def projectlist(request):
#     project = get_object_or_404(models.Project.objects.all())
#     data = {
#         "project": project,
#     }

#     return render(request, "projects.html", data)

def projectview(request):
    project = get_object_or_404(models.Project)
    data = {
        "project": project,
    }

    return render(request, "projects.html", data)
