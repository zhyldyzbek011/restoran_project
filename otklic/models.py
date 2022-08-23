from django.contrib.auth import get_user_model
from django.db import models

from vakansii.models import Vacansii

User = get_user_model()

class Otklic(models.Model):
    vakansii = models.ForeignKey(Vacansii, on_delete=models.CASCADE, related_name='vakansii')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otklic')

    class Meta:
        unique_together = ['vakansii', 'user']





