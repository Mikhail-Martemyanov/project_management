from django.db import models


class User(models.Model):
    EMPLOYEE_CHOICES = [
        ('m', 'Менеджер'),
        ('k', 'Консультант'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя сотрудника')
    employee = models.CharField(max_length=1, choices=EMPLOYEE_CHOICES, default='k', verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотруднки'
