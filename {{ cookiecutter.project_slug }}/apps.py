from django.apps import AppConfig


class {{ cookiecutter.project_slug.split("_")|map("title")|join("") }}Config(AppConfig):
    name = '{{ cookiecutter.project_slug }}'
