from django.db.models import Model, CharField, DateTimeField, EmailField, URLField
from django.utils.timezone import now


class Beneficiary(Model):
    """
    class representing a Beneficiary.

    A Beneficiary is represented by his/her name, an avatar URL, the email of the person who created this
    Beneficiary entry, and the entry's creation date.

    Attributes:
        - name: the name of the beneficiary. It must be a maximum of 255 characters.
        - avatar_url: the URL to the avatar (logo/picture) tied to the beneficiary. If not provided, a default URL is used.
        - creator_email: email of the person who created this entry. Can be null or blank.
        - creation_date: the date when this entry was created. This field is not editable and defaults to the current date and time.

    Methods:
        - __str__ : returns the name of the beneficiary as a string representation of the object
    """
    name = CharField(max_length=255)
    avatar_url = URLField(default='https://cdn.pixabay.com/photo/2023/03/17/20/42/camera-7859402_960_720.jpg')
    creator_email = EmailField(null=True, blank=True)
    creation_date = DateTimeField(default=now, editable=False)

    def __str__(self):
        """
        Returns a string representation of the Beneficiary model instance.

        Returns:
            str: The name of the beneficiary.
        """
        return str(self.name)
