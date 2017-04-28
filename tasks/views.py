from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView

from .models import Subject, Task

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = 'tasks'
    paginated_by = 10


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


