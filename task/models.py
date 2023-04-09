from django.db import models


# Create your models here.
class Task(models.Model):
    for_user = models.OneToOneField('user.User', on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name='выпоняет')  # id кому адресована задача

    text_task = models.TextField(verbose_name='задача')

    author_task = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                    null=True, related_name='author_tasks',
                                    verbose_name='задание выдал')  # id автора задачи

    status = models.BooleanField(default=False, verbose_name='статус')

    class Meta():
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
