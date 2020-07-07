from django.apps import AppConfig


class CrudAppConfig(AppConfig):
    name = 'crud_app'

    def ready(self):
        import crud_app.signals