from django.views.generic import ListView, DetailView, FormView

from .models import Task
from .forms import FilterForm

from django_filters.views import FilterView

# Create your views here.


class TaskListView(FilterView):
    """
    View to display list of task
    """
    model = Task
    filterset_class = FilterForm
    template_name = "tasks/tasks_list.html"
    context_object_name = 'tasks'
    paginated_by = 10




class TaskDetailView(DetailView):
    """
    View to display detail information about task
    """
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


