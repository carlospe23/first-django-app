from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'projects.html', context)


def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context)


def create_task(request):

    if request.method == 'GET':
        context = {
            'task_form': CreateNewTask()
        }
        return render(request, 'create_task.html', context)

    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2
        )
        return redirect('tasks')

def create_project(request):

    if request.method == 'GET':
        context = {
            'form_project': CreateNewProject()
        }
        return render(request, 'create_project.html', context)
    else:
        Project.objects.create(
            title=request.POST['title'],
        )
        return redirect('index')