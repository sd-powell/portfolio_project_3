from django.apps import AppConfig


class RecordsConfig(AppConfig):
    """
    Configuration for the 'records' app.

    Sets default primary key field type and identifies the app name.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "records"
