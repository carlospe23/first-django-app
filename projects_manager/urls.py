from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_tasks/', views.create_task, name='new_task'),
    path('create_project', views.create_project, name='new_project')

]