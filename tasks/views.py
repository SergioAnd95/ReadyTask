from django.views.generic import ListView, DetailView, FormView

from .models import Task

# Create your views here.


class TaskListView(ListView):
    """
    View to display list of task
    """
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = 'tasks'
    paginated_by = 10


class TaskDetailView(DetailView):
    """
    View to diplay detail information about task
    """
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


