# Generated by Django 3.0.10 on 2020-11-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_auto_20201104_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationunit',
            name='fixed_resources',
        ),
        migrations.RemoveField(
            model_name='reservationunit',
            name='movable_resources',
        ),
    ]
