from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from apps.core.views import frontpage, terms, contact, privacy, plans, signup

urlpatterns = [
                  #
                  # Urls
                  path('', frontpage, name='frontpage'),
                  path('privacy/', privacy, name='privacy'),
                  path('contact/', contact, name='contact'),
                  path('terms/', terms, name='terms'),
                  path('plans/', plans, name='plans'),
                  path('admin/', admin.site.urls),

                  #
                  # Dashboard
                  path('dashboard/', include('apps.dashboard.urls')),

                  #
                  # Auth
                  path('signup/', signup, name='signup'),
                  path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
