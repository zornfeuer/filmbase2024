from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notifications.models import Notification, NotificationSetting
from notifications.forms import NotificationSettingForm


@login_required
def notifications_view(request):
    if request.method == 'POST':
        # Обработка отметки уведомлений как прочитанных
        notification_ids = request.POST.getlist('notification_ids')
        Notification.objects.filter(
                id__in=notification_ids,
                user=request.user).update(is_read=True)

    # Получение уведомлений
    show_read = request.POST.get('show_read', 'off') == 'on'
    notifications = Notification.objects.filter(user=request.user.id)
    if not show_read:
        notifications = notifications.filter(is_read=False)

    return render(request, 'notifications.html', {
        'notifications': notifications,
        'show_read': show_read,
    })


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
