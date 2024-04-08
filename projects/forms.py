from django import forms

from .models import Project, Todo, Task


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title']


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title']


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title']