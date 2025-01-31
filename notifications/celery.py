import os
from celery import Celery

os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'filmbase.settings'
        )

app = Celery('filmbase2024')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
