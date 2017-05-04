from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField

# Create your models here.


class Subject(models.Model):
    """Class to represent subject model"""

    name = models.CharField(_('Название предмета'), max_length=100)

    class Meta:
        verbose_name = _('Предмет')
        verbose_name_plural = _('Предметы')

    def __str__(self):
        return '%s' % self.name


class LevelGradute(models.Model):
    """Class to represent graduated level model"""

    name = models.CharField(_('Класс'), max_length=20)

    class Meta:
        verbose_name = _('Класс')
        verbose_name_plural = _('Классы')

    def __str__(self):
        return '%s' % self.name


class Task(models.Model):
    """Class to represent task model"""

    EASY_LEVEL, NORMAL_LEVEL, HARD_LEVEL, OLYMP_LEVEL = 1, 2, 3, 4

    DIFFICULTY_LEVELS = (
        (EASY_LEVEL, _('Прсотой')),
        (NORMAL_LEVEL, _('Средний')),
        (HARD_LEVEL, _('Сложный')),
        (OLYMP_LEVEL, _('Олимпиадный'))
    )

    name = models.CharField(_('Название'), max_length=100)
    short_description = RichTextField(_('Краткое описание'))
    task_text = RichTextField(_('Описание задания'))

    answer_text = RichTextField(_('Ответ на задание'), null=True, blank=True)

    when_created = models.DateTimeField(_('Когда создан'), auto_now_add=True)
    when_updated = models.DateTimeField(_('Когда обновлено'), auto_now=True)

    subject = models.ForeignKey(Subject, verbose_name=_('Предмет'), related_name='subject_tasks')
    level_grad = models.ForeignKey(LevelGradute, verbose_name=_('Класс'), related_name='grad_tasks')

    difficult_level = models.IntegerField(_('Уровень сложности'), choices=DIFFICULTY_LEVELS)

    price = models.DecimalField(_('Стоимость'), decimal_places=2, max_digits=12)

    class Meta:
        verbose_name = _('Задание')
        verbose_name_plural = _('Задания')

        get_latest_by = '-when_created'
        ordering = ['-when_created', ]

    def __str__(self):
        return '%s' % self.name