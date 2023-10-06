from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import createNewTask
# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request,'index.html', {
        'title':title
    })

def hello(request, id):
    print(id)
    return HttpResponse('<h2>Hello %s</h2>' % id)

def about(request):
    username = 'mike'
    return render(request, 'about.html', {
        'username':username
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects':projects
        })

def tasks(request):
   # task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
       'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{
        'form':createNewTask()
     })
    else:
        Task.objects.create(title=request.POST['title'],
        description = request.POST['description'], projectkey=2)
        return redirect('/tasks/')
     