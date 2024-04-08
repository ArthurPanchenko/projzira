from django.contrib import admin
from .models import Project, Todo, Task


admin.site.register(Project)
admin.site.register(Todo)
admin.site.register(Task)

