from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BeneficiaryViewSet, CurrentUserAPIView

router = DefaultRouter()
router.register(r'beneficiaries', BeneficiaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/me/', CurrentUserAPIView.as_view(), name='current-user'),
]
