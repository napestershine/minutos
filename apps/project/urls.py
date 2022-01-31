from django.urls import path

from apps.project.views import projects

app_name = 'project'

urlpatterns = [
    path('', projects, name='projects')
]