# Generated by Django 3.0.10 on 2020-12-15 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_units', '0003_reservationunitimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationUnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='reservationunit',
            name='reservation_unit_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservation_units', to='reservation_units.ReservationUnitType', verbose_name='Type'),
        ),
    ]
