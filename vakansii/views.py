from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.permissions import IsAuthor
from otklic.models import Otclik

from vakansii.models import Vacansii
from . import serializers, permissions
from .serializers import VakansiiSerializer, UserVakansiiSerializer


class VacansiiViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Vacansii.objects.all()
    serializer_class = VakansiiSerializer
    #

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserVacansiiList(generics.ListAPIView):
    """Все объявления пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserVakansiiSerializer

    def get_queryset(self):
        return Vacansii.objects.filter(owner=self.request.user)


    @action(['GET'], detail=True)
    def otclik(self, request, pk):
        vakansii = self.get_object()
        otclik = vakansii.otclik.all()
        serializer = serializers.OtclikSerializer(otclik, many=True)
        return Response(serializer.data)

