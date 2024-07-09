from rest_framework import viewsets
from .models import Beneficiary
from .serializers import BeneficiarySerializer
from rest_framework.permissions import IsAuthenticated


class BeneficiaryViewSet(viewsets.ModelViewSet):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    permission_classes = [IsAuthenticated]
