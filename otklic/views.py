from rest_framework import generics



from otklic.models import Otclik
from otklic.permissions import IsAuthor
from vakansii import serializers, permissions


class OtclikListCreateView(generics.ListCreateAPIView):
    queryset = Otclik.objects.all()
    serializer_class = serializers.OtclikSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class OtclikDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = Otclik.objects.all()
    serializer_class = serializers.OtclikSerializer

    class Meta:
        model = Otclik
        exclude = 'otclik_detail'


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)