from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from notifications.models import NotificationSetting, Notification
from notifications.utils import send_email_notification


@shared_task
def send_immediate():
    users = NotificationSetting.objects.filter(frequency='immediate')

    for setting in users:
        notifications = Notification.objects.filter(
                user=setting.user, is_sent=False
        )
        for notification in notifications:
            send_email_notification(setting.user, notification.message)
            notification.is_sent = True
            notification.save()


@shared_task
def send_weekly():
    now = timezone.now()
    users = NotificationSetting.objects.filter(frequency='weekly')
    for setting in users:
        notifications = Notification.objects.filter(
                user=setting.user, is_sent=False
        )
        message = "У вас есть новые уведомления:\n\n"
        for notification in notifications:
            if now - notification.created_at <= timedelta(weeks=1):
                message += f"- {notification.message}\n"
                notification.is_sent = True
                notification.save()
        send_email_notification(setting.user, message)


@shared_task
def send_montly():
    now = timezone.now()
    users = NotificationSetting.objects.filter(frequency='montly')
    for setting in users:
        notifications = Notification.objects.filter(
                user=setting.user, is_sent=False
        )
        message = "У вас есть новые уведомления:\n\n"
        for notification in notifications:
            if now - notification.created_at <= timedelta(days=30):
                message += f"- {notification.message}\n"
                notification.is_sent = True
                notification.save()
        send_email_notification(setting.user, message)
