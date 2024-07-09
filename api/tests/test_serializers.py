from django.test import TestCase
from ..models import Beneficiary
from ..serializers import BeneficiarySerializer


class BeneficiarySerializerTest(TestCase):
    """
    Test module for BeneficiarySerializer class.

    BeneficiarySerializerTest is derived from django.test.TestCase, which
    is the base class for all the Django Test cases. This class defines
    the test suite for the BeneficiarySerializer class.

    At the beginning of the test, it sets up dummy data for the
    'beneficiary' object and 'serializer' object which are used
    throughout the test methods.

    Attributes:
    - beneficiary_attributes: a dictionary containing sample attributes of a Beneficiary instance.
    - serializer_data: a dictionary containing serialized data of a Beneficiary instance.
    - beneficiary: an instance of Beneficiary model created from 'beneficiary_attributes'.
    - serializer: an instance of BeneficiarySerializer initialized with 'beneficiary' instance.

    Methods:
    - setUp(): Initiate test setup
    - test_contains_expected_fields(): Test to check if all expected fields are contained in the serialized data.
    - test_name_field_content(): Test to check if the 'name' field in the serialized data matches the actual value.
    - test_avatar_url_field_content(): Test to check if the 'avatar_url' field in the serialized data matches the actual value.

    """

    def setUp(self):
        """
        Test set up method. This method runs before
        every test method to set up the test environment.
        """
        self.beneficiary_attributes = {'name': 'Jane Doe', 'avatar_url': 'https://example.com/avatar.jpg'}
        self.serializer_data = {'name': 'Jane Doe', 'avatar_url': 'https://example.com/avatar.jpg'}
        self.beneficiary = Beneficiary.objects.create(**self.beneficiary_attributes)
        self.serializer = BeneficiarySerializer(instance=self.beneficiary)

    def test_contains_expected_fields(self):
        """
        Method to test the presence of all expected fields
        in the serialized data.
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'avatar_url', 'creator_email', 'creation_date'})

    def test_name_field_content(self):
        """
        Method to test if the 'name' field in the serialized data
        matches with the 'name' field in source instance.
        """
        data = self.serializer.data
        self.assertEqual(data['name'], self.beneficiary.name)

    def test_avatar_url_field_content(self):
        """
        Method to test if the 'avatar_url' field in serialized data
        matches with the 'avatar_url' field in source instance.
        """
        data = self.serializer.data
        self.assertEqual(data['avatar_url'], self.beneficiary.avatar_url)
