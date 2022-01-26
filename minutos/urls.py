from django.contrib import admin
from django.urls import path

from apps.core.views import frontpage, terms, contact, privacy, plans

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('privacy/', privacy, name='privacy'),
    path('contact/', contact, name='contact'),
    path('terms/', terms, name='terms'),
    path('plans/', plans, name='plans'),
    path('admin/', admin.site.urls),
]
