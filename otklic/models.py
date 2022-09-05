
from django.db import models

from account.serializers import User
from vakansii.models import Vacansii



class Otclik(models.Model):
    owner = models.ForeignKey(User, related_name='otclik', on_delete=models.CASCADE)
    vakansii = models.ForeignKey(Vacansii, related_name='otclik', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # link = models.URLField(max_length=200, verbose_name='ссылка на вакансию')

    def __str__(self) -> str:
        return f'{self.owner} -> {self.vakansii} -> {self.created_at}'

