from django.core.mail import send_mail
from django.conf import settings
from notifications.models import NotificationSetting


def send_email_notification(user, message):
    user_mail = NotificationSetting.user_mail.filter(user=user.id)
    send_mail(
            'Уведомление из Каталога Фильмов',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user_mail],
            fail_silently=False,
    )
