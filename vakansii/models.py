from django.db import models
from django.shortcuts import reverse

from account.serializers import User
from transliteration import transliteration_rus_eng

JOB_TITLE = [
    ('Администратор', 'Администратор'),
    ('Официант', 'Официант'),
    ('Бармен', 'Бармен'),
    ('Уборщица', 'Уборщица'),
    ('Посудамойщица', 'Посудамойщица'),
    ('Повар', 'Повар'),
    ('Шеф-повар', 'Шеф-повар'),
    ('Хостес', 'Хостес')
]


CITY = [
    ('Бишкек', 'Бишкек'),
    ('Чуй', 'Чуй'),
    ('Нарын', 'Нарын'),
    ('Ысык-Кол', 'Ысык-Кол'),
    ('Баткен', 'Баткен'),
    ('Талас', 'Талас'),
    ('Ош', 'Ош'),
    ('Другой город', 'Другой город')
]
class Vacansii(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    job_title = models.CharField(max_length=100, choices=JOB_TITLE,  null=True, verbose_name='Должность')
    requirement = models.CharField(max_length=150, null=True, verbose_name='Требования')
    responsibilities = models.CharField(max_length=300, null=True, verbose_name='Обязанности')
    terms = models.CharField(max_length=150, null=True, verbose_name='Условия')
    income = models.CharField(max_length=150, null=True, verbose_name='Доход')
    city = models.CharField(max_length=150,choices=CITY, null=True, verbose_name='Город')
    contact_person = models.CharField(max_length=150, verbose_name='Контактное лицо')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField("url", max_length=200, unique=True)


    def save(self, *args, **kwargs):
        # TODO Доработать "slug = subject + id"
        self.slug = transliteration_rus_eng(self.job_title) + "_" + str(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse("advert-detail", kwargs={"category": self.category.slug, "slug": self.slug})

    class Meta:
        verbose_name_plural = 'Создать ваканцию'


class FilterVakansii(models.Model):
    """Фильтры"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"


