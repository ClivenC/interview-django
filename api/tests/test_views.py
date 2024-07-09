from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.contrib.auth import get_user_model

from api.models import Beneficiary
from api.serializers import BeneficiarySerializer

User = get_user_model()


class BeneficiaryAPITest(APITestCase):
    """
    Test suite for the API endpoints associated with the Beneficiary model.

    This class tests the CRUD operations performed on the Beneficiary model via API requests.

    Attributes:
    - user : Test user for authentication
    - token : Token for the test user
    - beneficiary : An instance of Beneficiary model
    - valid_payload : A dict containing sample Beneficiary payload
    - invalid_payload : A dict containing Beneficiary payload with invalid data

    Methods:
    - setUp(): Set up the test environment.
    - test_get_all_beneficiaries(): Test the API endpoint to get all beneficiaries.
    - test_create_valid_beneficiary(): Test the API endpoint to create a beneficiary with valid data.
    - test_create_invalid_beneficiary(): Test the API endpoint to create a beneficiary with invalid data.
    """

    def setUp(self):
        """
        Define the test variables and initialize test data.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.beneficiary = Beneficiary.objects.create(
            name="John Doe",
            avatar_url="https://example.com/avatar.jpg",
            creator_email="test@test.fr"
        )
        self.valid_payload = {
            'name': 'Jane Doe',
            'avatar_url': 'https://example.com/avatar.jpg',
            'creator_email': 'test@test.fr'
        }
        self.invalid_payload = {
            'name': '',
            'avatar_url': 'https://example.com/avatar.jpg',
            'creator_email': 'test@test.fr',
        }

    def test_get_all_beneficiaries(self):
        """
        Test the API endpoint to get all beneficiaries.

        For this test, the expected result is the Beneficiary instance created in the setUp.
        We check for the status_code to be 200 (HTTP_200_OK) and the response data to match
        the serialized data of our Beneficiary instance.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(reverse('beneficiary-list'))
        beneficiaries = Beneficiary.objects.all()
        serializer = BeneficiarySerializer(beneficiaries, many=True)

        print("Response Data: ", response.data)
        print("Serializer Data: ", serializer.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(serializer.data))

        for response_item, serializer_item in zip(response.data, serializer.data):
            self.assertEqual(response_item.get('id'), serializer_item.get('id'))
            self.assertEqual(response_item.get('name'), serializer_item.get('name'))
            self.assertEqual(response_item.get('avatar_url'), serializer_item.get('avatar_url'))

    def test_create_valid_beneficiary(self):
        """
        Test the API endpoint to create a beneficiary with valid data.

        Firstly, we attempt a POST request without authentication and expect to receive
        an HTTP_401_UNAUTHORIZED response.

        Secondly, we attempt a POST request with proper authentication and valid payload
        and expect to receive a HTTP_201_CREATED response.
        """

        # Authentication not provided Request must fail
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid auth')
        response = self.client.post(
            reverse('beneficiary-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authentication provided Request must success
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(
            reverse('beneficiary-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_beneficiary(self):
        """
        Test the API endpoint to create a beneficiary with invalid data.

        For this test, we attempt a POST request with authentication but with an invalid payload.
        The expected response status code is HTTP_400_BAD_REQUEST.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(
            reverse('beneficiary-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
