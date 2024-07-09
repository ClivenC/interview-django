from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Beneficiary


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Django's built-in User Model.

    UserSerializer is a ModelSerializer that takes the default User model
    and serializes it. It specifies the User model and what fields should be
    included in the serialized output.

    It includes the following fields: 'username', 'email'.
    """
    class Meta:
        model = User
        fields = ['username', 'email']

class BeneficiarySerializer(serializers.ModelSerializer):
    """
    Serializer for the Beneficiary model.

    The BeneficiarySerializer is a ModelSerializer which takes
    the Beneficiary model and serializes it. It specifies the Beneficiary
    model and what fields should be included in the serialized output.

    It includes the following fields: 'id', 'name', 'avatar_url', 'creator_email', 'creation_date'.
    """
    class Meta:
        model = Beneficiary
        fields = ['id', 'name', 'avatar_url', 'creator_email', 'creation_date']

