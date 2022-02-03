from django.urls import path

from apps.project.views import projects, project, edit_project, task, edit_task, edit_entry, delete_entry
from apps.project.views import delete_untracked_entry, track_entry
from .api import api_start_timer, api_stop_timer, api_discard_timer, api_get_tasks

app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),
    path('<int:project_id>/', project, name='project'),
    path('<int:project_id>/<int:task_id>/', task, name='task'),
    path('<int:project_id>/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/edit/', edit_entry, name='edit_entry'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/delete/', delete_entry, name='delete_entry'),
    path('<int:project_id>/edit/', edit_project, name='edit_project'),
    path('delete_untracked_entry<int:entry_id>', delete_untracked_entry, name='delete_untracked_entry'),
    path('track_entry<int:entry_id>', track_entry, name='track_entry'),

    # API

    path('api/start_timer/', api_start_timer, name='start_timer'),
    path('api/stop_timer/', api_stop_timer, name='stop_timer'),
    path('api/discard_timer/', api_discard_timer, name='discard_timer'),
    path('api/get_tasks/', api_get_tasks, name='get_tasks'),
]
