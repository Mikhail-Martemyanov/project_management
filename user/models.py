from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя сотрудника')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='должность')  # типа дожность

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'


class Category(models.Model):
    name_cat = models.CharField(max_length=100, verbose_name='должность')  # название должности

    def __str__(self):
        return self.name_cat

    class Meta():
        verbose_name = 'должность'
        verbose_name_plural = 'должность'


class Task(models.Model):
    for_user = models.OneToOneField('User', on_delete=models.SET_NULL, null=True, verbose_name='выпоняет')  # id кому адресована задача
    text_task = models.TextField(verbose_name='задача')
    author_task = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='author_tasks', verbose_name='задание выдал')  # id автора задачи
    status = models.BooleanField(default=False, verbose_name='статус')

    class Meta():
        verbose_name = 'Задача'
        verbose_name_plural = 'Задача'


class Message(models.Model):
    author_message = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, verbose_name='автор сообщения')  # id автора сообщения
    text_message = models.TextField(verbose_name='текст сообщения')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='время публикации')

    class Meta():
        verbose_name = 'собщение'
        verbose_name_plural = 'собщение'
