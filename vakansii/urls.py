from django.urls import path, include

from otklic import views
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('vacansii', views.VacansiiViewSet),
# router.register("<slug:slug>/", views.VacansiiViewSet, name='vakansii-detail')

urlpatterns = [
    path('', include(router.urls)),
    path('userVacansii/', views.UserVacansiiList.as_view()),
    path("<slug:slug>/", views.UserVacansiiList.as_view(), name="vakansii-detail"),
]