from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    slug = models.SlugField()
    position = models.ForeignKey(
        'Position',
        on_delete=models.DO_NOTHING,
        verbose_name='Должность'
    )
    date_of_employment = models.DateField('Дата приема на работу')
    salary = models.DecimalField('Размер ЗП', max_digits=8, decimal_places=2)
    division = TreeForeignKey(
        'Division',
        on_delete=models.PROTECT,
        related_name='division',
        verbose_name='Подразделение')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('employee-detail', args=[self.slug])


class Position(models.Model):
    title = models.CharField('Название должности', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Division(MPTTModel):
    title = models.CharField('Название подразделения', max_length=255)
    slug = models.SlugField()
    parent = TreeForeignKey(
        'self',
        blank=True, null=True,
        related_name='children',
        on_delete=models.SET_NULL
    )

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.slug

    def clean(self):
        if self.parent and self.parent.level > 5:
            raise ValidationError('cant create more 6 level')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('employees-by-division', args=[self.slug])
