from django.urls import path

from .views import add, team, edit, activate_team, invite, plans, plans_thankyou
from .api import create_checkout_session, stripe_webhooks

app_name = 'team'

urlpatterns = [
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
    path('invite/', invite, name='invite'),
    path('plans/', plans, name='plans'),
    path('plans/thank_you/', plans_thankyou, name='plans_thankyou'),
    path('activate_team/<int:team_id>/', activate_team, name='activate_team'),
    path('<int:team_id>/', team, name='team'),

    # api
    path('api/stripe_webhooks/', stripe_webhooks, name='stripe_webhooks'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
]
