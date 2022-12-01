from django.apps import AppConfig


class ReservesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.reserves"


    def ready(self):
        from . import signals