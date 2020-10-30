# Generated by Django 3.0.10 on 2020-10-30 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Building",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "area",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Area"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Space",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "area",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Area"
                    ),
                ),
                (
                    "building",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="spaces",
                        to="spaces.Building",
                        verbose_name="Building",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="spaces.Space",
                        verbose_name="Parent space",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="building",
            name="district",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="spaces.District",
                verbose_name="District",
            ),
        ),
    ]
