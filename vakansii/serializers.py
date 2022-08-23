from rest_framework import serializers

from vakansii.models import Vacansii


class VakansiiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacansii
        fields = '__all__'

