from django.db.models.signals import post_save
from django.dispatch import reciever

from notifications.models import NotificationSetting, Notification
from films.models import Movie, Actor


def create_notification_for_new_movie(movie):
    settings = NotificationSetting.objects.filter(notify_on_new_movie=True)
    message = f'Новый фильм "{movie.title}" в жанре "{movie.genre}".'

    for setting in settings:
        Notification.objects.create(user=setting.user, message=message)


def create_notification_for_movie_update(movie):
    settings = NotificationSetting.objects.filter(notify_on_movie_update=True)
    message = f'Обновлена информация о фильме "{movie.title}"'

    for setting in settings:
        Notification.objects.create(user=setting.user, message=message)


def create_notification_for_actor_update(actor):
    settings = NotificationSetting.objects.filter(notify_on_actor_update=True)
    message = f'Обновлена информация о {actor.name}'

    for setting in settings:
        if (setting.followed_actors.filter(id=actor.id).exists()
           or not setting.followed_actors.exists()):
            Notification.objects.create(user=setting.user, message=message)


@reciever(post_save, sender=Movie)
def movie_updated(sender, instance, created, **kwargs):
    if created:
        create_notification_for_new_movie(instance)
        return
    create_notification_for_movie_update(instance)


@reciever(post_save, sender=Actor)
def actor_updated(sender, instance, created, **kwargs):
    if created:
        return
    create_notification_for_actor_update(instance)
