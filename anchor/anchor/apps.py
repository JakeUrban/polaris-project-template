from django.apps import AppConfig


class AnchorConfig(AppConfig):
    name = "anchor"
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        from polaris.integrations import register_integrations

        # pass your integration functions and subclasses here
        # see https://django-polaris.readthedocs.io/en/stable/register_integrations/index.html
        register_integrations()
