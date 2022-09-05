from rest_framework import serializers

from reziume.models import Reziume
from vakansii.models import Vacansii


class ReziumeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Reziume
        fields = '__all__'

