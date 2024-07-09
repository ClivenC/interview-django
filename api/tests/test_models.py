from django.test import TestCase
from api.models import Beneficiary


class BeneficiaryModelTest(TestCase):
    """
     Test suite for the Beneficiary model.

     The BeneficiaryModelTest class contains test cases for the Beneficiary model.
     It tests basic operations such as model instance creation and string representation.

     Attributes:
     - beneficiary : An instance of Beneficiary model

     Methods:
     - setUp(): Set up test data for the tests.
     - test_beneficiary_creation(): Test case for creating a Beneficiary instance.
     - test_beneficiary_str(): Test case for the string representation of Beneficiary instance.
     """

    def setUp(self):
        """
        Put the initial set up configuration code for your tests here.
        This method is called before the execution of each test case.
        """
        self.beneficiary = Beneficiary.objects.create(
            name="John Doe",
            avatar_url="https://example.com/avatar.jpg",
            creator_email="test@test.fr"
        )

    def test_beneficiary_creation(self):
        """
        Test case for creating a Beneficiary instance.

        The test checks if the instance is properly created by comparing the
        attributes of the instance with the original data.
        """
        self.assertEqual(self.beneficiary.name, "John Doe")
        self.assertEqual(self.beneficiary.avatar_url, "https://example.com/avatar.jpg")
        self.assertEqual(self.beneficiary.creator_email, "test@test.fr")

    def test_beneficiary_str(self):
        """
        Test case for the string representation of Beneficiary instance.

        The test checks if the __str__ method of Beneficiary model is correctly implemented.
        For Beneficiary, the expectation is that it should return the name of the Beneficiary.
        """
        self.assertEqual(str(self.beneficiary), "John Doe")
