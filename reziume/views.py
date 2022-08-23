from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from . import serializers
from vakansii.models import Vacansii
from .models import Reziume
from .serializers import ReziumeSerializer


class ReziumeViewSet(ModelViewSet):
    queryset = Reziume.objects.all()
    serializer_class = ReziumeSerializer
    #
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


