# Generated by Django 3.0.10 on 2020-11-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="buffer_time_after",
            field=models.DurationField(
                blank=True, null=True, verbose_name="Buffer time after"
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="buffer_time_before",
            field=models.DurationField(
                blank=True, null=True, verbose_name="Buffer time before"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(
                choices=[
                    ("introduction", "Introduction"),
                    ("catering", "Catering"),
                    ("configuration", "Configuration"),
                ],
                default="introduction",
                max_length=255,
                verbose_name="Name",
            ),
        ),
    ]
