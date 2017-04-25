from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LevelGradute)
class LevelGraduteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'when_created', 'level_grad', 'subject', 'difficult_level')
    list_filter = ('difficult_level', 'subject', 'level_grad')
    search_fields = ('name', 'task_text', 'short_description')

