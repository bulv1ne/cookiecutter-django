from django.urls import path

from . import views

app_name = '{{ cookiecutter.project_slug }}'


urlpatterns = [
    path('', views.IndexView.as_view()),
]
