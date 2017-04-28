from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView

from tasks.models import Task
# Create your views here.


@csrf_protect
@require_POST
def add_task_to_basket(request, pk):
    """
    view to add task to basket
    :param request: HttpRequest
    :param pk: int
    :return: HttpResponse
    """
    task = get_object_or_404(Task, pk=pk)
    request.basket.add_task(task)
    success_url = request.META['HTTP_REFERER']
    return redirect(success_url)


@csrf_protect
@require_POST
def remove_task_from_basket(request, pk):
    """
    view to remove task from basket
    :param request: HttpRequest
    :param pk: int
    :return: HttpResponse
    """
    basket_line = get_object_or_404(request.basket.lines, task__pk=pk)
    # line = request.basket.lines.get
    basket_line.delete()
    success_url = request.META['HTTP_REFERER']
    return redirect(success_url)
