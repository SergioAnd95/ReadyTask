from django import forms

from .models import Subject, LevelGradute, Task

import django_filters


class FilterForm(django_filters.FilterSet):
    """
    Class Form to represent filter form of Task
    """
    subject = django_filters.ModelMultipleChoiceFilter(
        widget=forms.CheckboxSelectMultiple,
        queryset=Subject.objects.all(),
        required=False
    )
    level_grad = django_filters.ModelMultipleChoiceFilter(
        widget=forms.CheckboxSelectMultiple,
        queryset=LevelGradute.objects.all(),
        required=False
    )

    class Meta:
        model = Task
        fields = ('subject', 'level_grad')