

from rest_framework import serializers
import vakansii
from account.permissions import IsAuthor
from otklic.models import Otclik

from vakansii import permissions

from vakansii.models import Vacansii, FilterVakansii


class OtclikSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Otclik
        fields = ('id', 'body', 'owner', 'vakansii')



class VakansiiSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Vacansii
        fields = '__all__'

class UserVakansiiSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Vacansii
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['otclik_detail'] = OtclikSerializer(instance.otclik.all(), many=True).data
        return representation


class FilterAdvertSer(serializers.ModelSerializer):
    """Для вывода фильтров"""
    class Meta:
        model = FilterVakansii
        fields = ("name", )


