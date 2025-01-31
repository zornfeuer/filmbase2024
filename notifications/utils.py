from django.core.mail import send_mail
from notifications.models import NotificationSetting


def send_email_notification(recipient, message):
    user_mail = NotificationSetting.objects.filter(
            user=recipient.id)[0].user_mail
    if user_mail:
        print(f"Sending email to: {user_mail}")  # Отладочное сообщение
        send_mail(
            'Уведомление из Каталога Фильмов',
            message,
            from_email=None,
            recipient_list=[user_mail],
            fail_silently=False,
        )
    else:
        print("No email found for user.")
