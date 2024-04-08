from django.urls import path

from . import views


urlpatterns = [
    path('projects/', views.projectsView, name='projects-list'),
    path('project/<uuid:uuid>/', views.projectDetailView, name='project-detail'),
    path('project/<uuid:uuid>/update', views.updateProjectView, name='update-project'),
    path('project/create-todo/', views.createTodo, name='create-todo'),
    path('project/<uuid:uuid>/todo/<int:pk>/', views.todoDetail, name='todo-detail'),
    path('project/update-task/<int:pk>/', views.updateTask, name='update-task')
]