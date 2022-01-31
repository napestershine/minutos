from django.contrib import admin

from apps.project.models import Project, Task

admin.site.register(Project)
admin.site.register(Task)
