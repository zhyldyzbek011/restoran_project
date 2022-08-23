from rest_framework import serializers

import vakansii
from vakansii.models import Vacansii


class VakansiiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacansii
        fields = '__all__'

    def otklic(self, vakansii):
        user = self.context.get('request').user
        return user.otklic.filter(vakansii=vakansii).exists()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['otklic'] = self.otklic(instance)

        representation['otklic_count'] = instance.vakansii.count()
        return representation
