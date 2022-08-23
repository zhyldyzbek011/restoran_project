from django.db import models

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
    job_title = models.CharField(max_length=100, choices=JOB_TITLE,  null=True, verbose_name='Должность')
    requirement = models.CharField(max_length=150, null=True, verbose_name='Требования')
    responsibilities = models.CharField(max_length=300, null=True, verbose_name='Обязанности')
    terms = models.CharField(max_length=150, null=True, verbose_name='Условия')
    income = models.CharField(max_length=150, null=True, verbose_name='Доход')
    city = models.CharField(max_length=150,choices=CITY, null=True, verbose_name='Город')
    contact_person = models.CharField(max_length=150, verbose_name='Контактное лицо')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Создать ваканцию'

    def __str__(self):
        return str(self.job_title)





