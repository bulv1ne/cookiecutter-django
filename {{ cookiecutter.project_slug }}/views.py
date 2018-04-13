from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = '{{ cookiecutter.project_slug }}/index.html'
