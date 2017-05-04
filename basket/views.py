from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView

import json

from tasks.models import Task
# Create your views here.


class BasketView(TemplateView):
    template_name = 'basket/basket.html'

@require_POST
@csrf_protect
def add_task_to_basket(request, pk):
    """
    view to add task to basket
    :param request: HttpRequest
    :param pk: int
    :return: HttpResponse
    """

    task = get_object_or_404(Task, pk=pk)
    request.basket.add_task(task)
    if request.is_ajax():
        return HttpResponse(request.basket.total_price_currency)
    else:
        success_url = request.META['HTTP_REFERER']
        return redirect(success_url)


@require_POST
@csrf_protect
def remove_task_from_basket(request, pk):
    """
    view to remove task from basket
    :param request: HttpRequest
    :param pk: int
    :return: HttpResponse
    """
    basket_line = get_object_or_404(request.basket.lines, task__pk=pk)
    basket_line.delete()
    if request.is_ajax():
        return HttpResponse(request.basket.total_price_currency)
    else:
        success_url = request.META['HTTP_REFERER']
        return redirect(success_url)
