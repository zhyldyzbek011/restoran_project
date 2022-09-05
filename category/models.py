from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

CHOISE = [
    ('Работадатель', 'Работадатель'),
    ('Ищу работу','Ищу работу')
]

class Category(MPTTModel):
    """Категории объявлений"""
    name = models.CharField(max_length=100, choices=CHOISE,  null=True, verbose_name='имя')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Родитель"
    )
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = "Категория"
