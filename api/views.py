import random

from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Beneficiary
from api.serializers import BeneficiarySerializer, UserSerializer

# List of real names
real_names = ['Emma', 'Olivia', 'Ava', 'Mia', 'Sophia', 'Isabella', 'Charlotte',
              'Amelia', 'Harper', 'Evelyn', 'Liam', 'Noah', 'William', 'James',
              'Oliver', 'Benjamin', 'Elijah', 'Lucas', 'Mason', 'Logan']


class CurrentUserAPIView(APIView):
    """
    API View to retrieve the current logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return details of the current logged-in user.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class BeneficiaryViewSet(viewsets.ModelViewSet):
    # pylint: disable=too-many-ancestors
    """
    Django ModelViewSet for Beneficiary model.

    The BeneficiaryViewSet class inherits from Django's ModelViewSet to provide actions/methods
    for operations such as list, create, retrieve, update and delete.

    This viewset also includes a custom method 'create_random' which is intended to create random beneficiary.

    Attributes:
    - queryset: Queryset containing all Beneficiary objects.
    - serializer_class: Serializer used for Beneficiary instances.
    - filter_backends: Filter backend used for searching the beneficiaries.
    - search_fields: Searchable fields in the Beneficiary model.

    Methods:
    - perform_create(serializer): Save the Serializer with the creator_email parameter.
    - create_random(request): Create a random Beneficiary object and save it to database.
    - destroy(request, *args, **kwargs): Delete the beneficiary object.
    - update(request, *args, **kwargs): Update the beneficiary object and save it to database.
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        """
        Overrides the perform_create method of Django's ModelViewSet.
        """
        user = self.request.user
        serializer.save(creator_email=user.email if user.is_authenticated else None)

    @action(detail=False, methods=['post'])
    def create_random(self, request) -> Response:
        """
        Overrides the create method of Django's ModelViewSet.
        Returns:
        - Response object with the serialized Beneficiary instance and HTTP_201_CREATED status.
        """
        random_name = random.choice(real_names)
        user = request.user
        avatar_url = f'https://api.dicebear.com/8.x/avataaars/svg?seed={random_name}'
        beneficiary = Beneficiary.objects.create(
            name=random_name,
            avatar_url=avatar_url,
            creator_email=user.email if user.is_authenticated else None
        )
        serializer = self.get_serializer(beneficiary)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Overrides the destroy method of Django's ModelViewSet.
        Returns:
        - Response object with HTTP_204_NO_CONTENT status.
        """
        beneficiary = self.get_object()
        beneficiary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        """
        Overrides the update method of Django's ModelViewSet.
        Returns:
        - Response object with the serialized Beneficiary data.
        """
        partial = kwargs.pop('partial', False)
        beneficiary = self.get_object()
        serializer = self.get_serializer(beneficiary, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
