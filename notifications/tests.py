# films/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from films.models import Film, Person, Country, Genre
from notifications.models import NotificationSetting, Notification
from notifications.utils import send_email_notification
from config import test_mail


class NotificationSignalTests(TestCase):

    def setUp(self):
        # Создание пользователя и настроек уведомлений
        self.user = User.objects.create_user(
                username='testuser',
                password='testpass'
                )
        self.notification_setting = NotificationSetting.objects.create(
            user=self.user,
            notify_on_new_movie=True,
            notify_on_movie_update=True,
            notify_on_actor_update=True,
            user_mail=test_mail,
        )

        # Создание необходимых объектов для тестов
        self.country = Country.objects.create(name='США')
        self.genre = Genre.objects.create(name='Драма')
        self.director = Person.objects.create(name='Режиссер Тест')
        # Создание нового фильма
        self.film = Film.objects.create(
            name='Тестовый фильм',
            country=self.country,
            director=self.director,
            year=2023
        )
        self.film.genres.add(self.genre)

    def test_create_notification_for_new_film(self):
        # Проверка, что уведомление было создано
        notifications = Notification.objects.filter(
                user=self.user,
                )
        self.assertEqual(
                notifications[0].message,
                f'Новый фильм "{self.film.name}".'
                )
        send_email_notification(self.user, notifications[0].message)

    def test_create_notification_for_film_update(self):

        # Обновление фильма
        self.film.year = 2024
        self.film.save()  # Сохраняем изменения

        # Проверка, что уведомление было создано
        notifications = Notification.objects.filter(
                user=self.user,
                )
        self.assertEqual(
                notifications[1].message,
                f'Обновлена информация о фильме "{self.film.name}"'
                )

    def test_create_notification_for_person_update(self):
        # Создание нового человека
        person = Person.objects.create(name='Тестовый человек')
        person.name = 'Обновленный человек'
        person.save()

        # Проверка, что уведомление было создано
        notifications = Notification.objects.filter(
                user=self.user,
                )
        self.assertEqual(
                notifications[1].message,
                f'Обновлена информация о {person.name}'
                )

    def test_no_notification_for_unfollowed_actor(self):
        # Создание нового человека
        person = Person.objects.create(name='Тестовый человек')
        self.notification_setting.people.clear()

        # Обновление человека
        person.name = 'Обновленный человек'
        person.save()

        # Проверка, что уведомление не было создано
        notifications = Notification.objects.filter(
                user=self.user
                )
        self.assertEqual(notifications.count(), 2)

    def test_notification_for_followed_actor(self):
        # Создание нового человека
        person = Person.objects.create(name='Тестовый человек')
        self.notification_setting.people.add(person)

        # Обновление человека
        person.name = 'Обновленный человек'
        person.save()

        # Проверка, что уведомление было создано
        # Проверка, что уведомление не было создано
        notifications = Notification.objects.filter(
                user=self.user,
                )
        self.assertEqual(
                notifications[1].message,
                f'Обновлена информация о {person.name}'
                )
