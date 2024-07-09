from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Django AppConfig class for the 'api' application.

    The ApiConfig class is a subclass of Django's AppConfig, used to configure the name of the application.
    It is used to hold the configuration for the 'api' application and also to keep any application specific settings.

    Attributes:
    - name: the name of the application. It must be unique across a Django project.

    There are no methods defined in this class as it's purpose is configuration and it doesn't have operational responsibility.
    """
    name = 'api'
