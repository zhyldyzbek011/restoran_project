from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet

from . import serializers
from vakansii.models import Vacansii
from .models import Reziume
from .serializers import ReziumeSerializer


class ReziumeViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reziume.objects.all()
    serializer_class = ReziumeSerializer
    #

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
