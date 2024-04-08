from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from .models import Project, Todo, Task
from .forms import ProjectForm, TodoForm, TaskForm


def send_post_form(request, form, root_name, root):
    form = form(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        setattr(instance, root_name, root)
        instance.save()
        return instance


@login_required
def projectsView(request):
    if request.method == 'POST':
        instance = send_post_form(request, ProjectForm, 'author', request.user)
        return redirect(instance.get_absolute_url())
    else:
        form = ProjectForm()
        context = {'form': form}
        projs = Project.objects.filter(author=request.user)
        context['projects'] = projs
    
    return render(request, 'projects/projects.html', context)


def projectDetailView(request, uuid):
    project = Project.objects.get(uuid=uuid)
    update_form = ProjectForm(instance=project)
    todo_form = TodoForm()

    context = {
        'project': project,
        'update_form': update_form,
        'todo_form': todo_form,
        'todos': project.todo_set.all()
    } 
    return render(request, 'projects/project-detail.html', context)


def updateProjectView(request, uuid):
    if request.method == 'POST':
        proj = Project.objects.get(uuid=uuid)
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            instance = form.save()
        return redirect(instance.get_absolute_url())


def createTodo(request):
    if request.method == 'POST':
        project = Project.objects.get(uuid=request.POST.get('project'))
        send_post_form(request, TodoForm, 'project', project)
    return redirect(project.get_absolute_url())


def todoDetail(request, uuid, pk):

    todo = Todo.objects.get(pk=pk)
    create_task_form = TaskForm()
    context = {
        'todo': todo,
        'task_form': create_task_form,
    }
    

    if request.method == 'POST':
        send_post_form(request, TaskForm, 'todolist', todo)
        return redirect(todo.get_absolute_url())

    return render(request, 'projects/todo-detail.html', context)


def updateTask(request, pk):
    
    task = Task.objects.get(pk=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return redirect(task.todolist.get_absolute_url())

