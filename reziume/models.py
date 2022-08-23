from django.db import models


class Reziume(models.Model):
    name = models.CharField(max_length=140, verbose_name='Имя')
    lust_name = models.CharField(max_length=140, verbose_name='Фамилия')
    number_phone = models.CharField(max_length=50, verbose_name='номер телефона', default='+996')
    email = models.EmailField(verbose_name='електронная почта')
    age = models.IntegerField(verbose_name='возраст')
    education = models.CharField(max_length=140, verbose_name='Образование')
    languages = models.TextField(max_length=150, verbose_name='языки которыми вы владеете')
    experience = models.CharField(max_length=150, verbose_name='Опыт работы')
    personal_info = models.TextField(max_length=500, verbose_name='О себе')

    class Meta:
        verbose_name_plural = 'Добавить резюме'

    def __str__(self): return self.email





