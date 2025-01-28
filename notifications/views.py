from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notifications.models import Notification, NotificationSetting
from notifications.forms import NotificationSettingForm


def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user.id).order_by(
            'created_at')
    return render(request, 'notifications.html',
                  {'notifications': notifications})


@login_required
def notification_settings_view(request):
    notification_settings, created = (
            NotificationSetting.objects.get_or_create(user=request.user)
            )

    if request.method == 'POST':
        form = NotificationSettingForm(
                request.POST,
                instance=notification_settings
                )
        if form.is_valid():
            form.save()
            messages.success(request, 'Настройки успешно сохранены!')
            return redirect('notifications:settings')
    else:
        form = NotificationSettingForm(instance=notification_settings)

    return render(request, 'settings.html',
                  {'form': form})
