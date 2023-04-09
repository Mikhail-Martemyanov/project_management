from django.db import models
from user.models import User

# Create your models here.
class Message(models.Model):
    author_message = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True,
                                       verbose_name='автор сообщения')  # id автора сообщения

    text_message = models.TextField(verbose_name='текст сообщения')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='время публикации')

    class Meta():
        verbose_name = 'собщение'
        verbose_name_plural = 'собщений'
