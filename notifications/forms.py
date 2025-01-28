from django import forms
from notifications.models import NotificationSetting


class NotificationSettingForm(forms.ModelForm):
    class Meta:
        model = NotificationSetting
        fields = [
            'user_mail',
            'notify_on_movie_update',
            'notify_on_new_movie',
            'notify_on_actor_update',
            'followed_actors',
            'frequency',
        ]
        widgets = {
                'followed_actors': forms.SelectMultiple(attrs={
                        'class': 'form-select',
                        'size': '5'
                    }),
        }

    def __init__(self, *args, **kwargs):
        super(NotificationSettingForm, self).__init__(*args, **kwargs)
        self.fields['notify_on_movie_update'].label = \
            "Уведомлять об изменениях страниц фильмов?"
        self.fields['notify_on_new_movie'].label = \
            "Уведомлять о новых фильмах?"
        self.fields['notify_on_actor_update'].label = \
            "Уведомлять об изменениях страниц актеров?"
        self.fields['followed_actors'].label = \
            "Актеры для подписки"
        self.fields['frequency'].label = "Частота уведомлений"
        self.fields['user_mail'].label = \
            "Почта для уведомлений"
