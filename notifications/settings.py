from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send-immediate': {
        'task': 'filmbase2024.signup.tasks.send_immediate',
        'schedule': crontab(minute='*/5'),
    },
    'send-weekly': {
        'task': 'filmbase2024.signup.tasks.send_weekly',
        'schedule': crontab(0, 0, day_of_week='mon'),
    },
    'send-monthly': {
        'task': 'filmbase2024.signup.tasks.send_monthly',
        'schedule': crontab(0, 0, day=1),
    },
}
