from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import NotificationSetting, Notification
from films.models import Film, Person


def create_notification_for_new_film(film):
    settings = NotificationSetting.objects.filter(notify_on_new_movie=True)
    message = f'Новый фильм "{film.name}".'

    for setting in settings:
        Notification.objects.create(user=setting.user, message=message)


def create_notification_for_film_update(film):
    settings = NotificationSetting.objects.filter(notify_on_movie_update=True)
    message = f'Обновлена информация о фильме "{film.name}"'

    for setting in settings:
        Notification.objects.create(user=setting.user, message=message)


def create_notification_for_person_update(person):
    settings = NotificationSetting.objects.filter(notify_on_actor_update=True)
    message = f'Обновлена информация о {person.name}'

    for setting in settings:
        if (setting.people.filter(id=person.id).exists()
           or not setting.people.exists()):
            Notification.objects.create(user=setting.user, message=message)


@receiver(post_save, sender=Film)
def film_updated(sender, instance, created, **kwargs):
    if created:
        create_notification_for_new_film(instance)
        return
    create_notification_for_film_update(instance)


@receiver(post_save, sender=Person)
def person_updated(sender, instance, created, **kwargs):
    if created:
        return
    create_notification_for_person_update(instance)
