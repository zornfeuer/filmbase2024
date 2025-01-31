# Generated by Django 5.1.5 on 2025-01-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notificationsetting_user_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsetting',
            name='frequency',
            field=models.CharField(choices=[('immediate', 'Незамедлительно'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=20),
        ),
    ]
