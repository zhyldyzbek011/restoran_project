from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from . import serializers
from vakansii.models import Vacansii
from .serializers import VakansiiSerializer


class VacansiiViewSet(ModelViewSet):
    queryset = Vacansii.objects.all()
    serializer_class = VakansiiSerializer
    #
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


