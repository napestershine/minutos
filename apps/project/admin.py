from django.contrib import admin

from apps.project.models import Project, Task, Entry

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Entry)
