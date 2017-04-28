from django import template

register = template.Library()


@register.filter
def basket_task_exist(task, basket):
    return basket.exist(task)