from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.permissions import IsAuthor
from otklic.models import Otklic
from . import serializers
from vakansii.models import Vacansii
from .serializers import VakansiiSerializer


class VacansiiViewSet(ModelViewSet):
    queryset = Vacansii.objects.all()
    serializer_class = VakansiiSerializer
    #
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(['POST'], detail=True)
    def add_to_otklic(self, request, pk):
        vakansii = self.get_object()
        if request.user.otklic.filter(vakansii=vakansii).exists():
            return Response('Вы уже откликнулись на эту вакансию!', status=status.HTTP_400_BAD_REQUEST)
        Otklic.objects.create(vakansii=vakansii, user=request.user)
        return Response('Вы успешно откликнулись', status=status.HTTP_201_CREATED)

    @action(['POST'], detail=True)
    def remove_from_otklic(self, request, pk):
        vakansii = self.get_object()
        if not request.user.otklic.filter(vakansii=vakansii).exists():
            return Response('Вы уже откликнулись на эту вакансию!', status=status.HTTP_400_BAD_REQUEST)
        request.user.otklic.filter(vakansii=vakansii).delete()
        Otklic.objects.create(vakansii=vakansii, user=request.user)
        return Response('Вы успешно удалили свой отклик', status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action in ('create',):
            return [permissions.IsAuthenticated(), ]

        elif self.action in ('update', 'partial_update', 'destroy,'):
            return [IsAuthor(), ]
        else:
            return [permissions.AllowAny(), ]