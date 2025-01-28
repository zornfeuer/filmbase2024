from django.urls import path
from notifications import views

app_name = "notifications"
urlpatterns = [
    path('', views.notifications_view, name='notifications'),
    path(
        'settings',
        views.notification_settings_view,
        name='settings'
    )
]
