default_app_config = '{{ cookiecutter.project_slug }}.apps.{{ cookiecutter.project_slug.split("_")|map("title")|join("") }}Config'
