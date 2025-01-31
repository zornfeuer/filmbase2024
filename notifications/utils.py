from django.core.mail import send_mail


def send_email_notification(user, message):
    if user.email:
        send_mail(
            'Уведомление из Каталога Фильмов',
            message,
            from_email=None,
            recipient_list=[user.email],
            fail_silently=False,
        )
