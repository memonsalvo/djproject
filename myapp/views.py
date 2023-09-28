from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    return render(request,'index.html')

def hello(request, id):
    print(id)
    return HttpResponse('<h2>Hello %s</h2>' % id)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
   # task = Task.objects.get(title=title)
    return render(request, 'tasks.html')