from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('otclik/', views.OtclikListCreateView.as_view()),
    path('otclik/<int:pk>/', views.OtclikDetailView.as_view()),
]