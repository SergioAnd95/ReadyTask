from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.core.exceptions import PermissionDenied
from django.conf import settings

from decimal import Decimal

# Create your models here.


class Basket(models.Model):

    OPEN, MERGED, SAVED, FROZEN, SUBMITTED = (
        "Open", "Merged", "Saved", "Frozen", "Submitted")
    STATUS_CHOICES = (
        (OPEN, _("Open - currently active")),
        (MERGED, _("Merged - superceded by another basket")),
        (SAVED, _("Saved - for items to be purchased later")),
        (FROZEN, _("Frozen - the basket cannot be modified")),
        (SUBMITTED, _("Submitted - has been ordered at the checkout")),
    )
    status = models.CharField(
        _("Статус"), max_length=128, default=OPEN, choices=STATUS_CHOICES)

    when_created = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')

    def add_task(self, task):
        """
        Add task to basket
        """
        added_task = self.lines.get_or_create(
            task=task
        )

        return added_task

    def remove_line(self, line):
        """
        Remove line from basket
        """
        if line in self.lines:
            line.delete()

    def flush(self):
        """
        Remove all lines from basket.
        """
        if self.status == self.FROZEN:
            raise PermissionDenied("A frozen basket cannot be flushed")
        self.lines.all().delete()

    def submit(self):
        """
        Mark this basket as submitted
        """
        self.status = self.SUBMITTED
        self.date_submitted = now()
        self.save()

    def exist(self, task):
        lines = self.lines.filter(task=task)
        if len(lines) == 0:
            return False
        else:
            return True

    @property
    def total_price(self):
        """
        Propery to provide total price in basket
        :return: Decimal
        """
        total = Decimal('0.00')
        for line in self.lines.all():
            total += line.price
        return total

    @property
    def total_price_currency(self):
        return '%s %s' %(self.total_price, settings.CURRENCY[1])


class BasketLine(models.Model):
    basket = models.ForeignKey(Basket, verbose_name=_('Корзина') ,related_name='lines')
    task = models.ForeignKey('tasks.Task', verbose_name=('Задание'))
    when_created = models.DateTimeField(_('Дата создание'), auto_now_add=True)

    @property
    def price(self):
        return self.task.price