# Generated by Django 5.1.3 on 2024-12-20 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationsetting',
            name='user_mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
