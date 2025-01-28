from django.db import models
from django.contrib.auth.models import User

from films.models import Person


class NotificationSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_mail = models.EmailField(max_length=254, blank=True, null=True)
    notify_on_movie_update = models.BooleanField(default=False)
    notify_on_new_movie = models.BooleanField(default=False)
    notify_on_actor_update = models.BooleanField(default=False)
    followed_actors = models.ManyToManyField(Person, blank=True)
    frequency = models.CharField(max_length=20, choices=[
        ('immediate', 'Сразу после внесения данных'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ])


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
