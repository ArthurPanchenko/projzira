from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TitleFieldModel(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Project(TitleFieldModel):
    """Model for project"""

    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'Project {self.title}'
    
    def get_absolute_url(self):
        return reverse('project-detail', args=[self.uuid])
    

class Todo(TitleFieldModel):
    """Model for todo list in project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.title}'s {self.title} todo"
    
    def get_absolute_url(self):
        return reverse('todo-detail', args=[self.project.uuid, self.pk])
    

class Task(TitleFieldModel):

    todolist = models.ForeignKey(Todo, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ['is_done']

    def __str__(self):
        return self.title