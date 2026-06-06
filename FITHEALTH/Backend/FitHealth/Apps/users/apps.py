from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Apps.users"

    def ready(self):
        import FITHEALTH.Backend.FitHealth.Apps.users.signals
