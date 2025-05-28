from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class abexam(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экзамена')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    exam_date = models.DateTimeField(verbose_name='Дата проведения экзамена')
    image = models.ImageField(upload_to='exam_images/', verbose_name='Изображение задания', null=True, blank=True)
    users = models.ManyToManyField(User, verbose_name='Пользователи, сдающие экзамен')
    is_public = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'