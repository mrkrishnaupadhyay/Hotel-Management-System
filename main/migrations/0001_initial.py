# Generated by Django 2.0.1 on 2018-01-21 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'permissions': (('can_view_customer', 'Can view customer'),),
                'ordering': ['first_name', 'middle_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_children', models.PositiveSmallIntegerField(default=0)),
                ('no_of_adults', models.PositiveSmallIntegerField(default=1)),
                ('reservation_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_arrival_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_departure_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Customer')),
                ('staff', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_view_reservation', 'Can view reservation'), ('can_view_reservation_detail', 'Can view reservation detail')),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[('SM', 'Simple'), ('DX', 'Deluxe'), ('PM', 'Premium')], default='SM', max_length=2)),
                ('availability', models.BooleanField(default=0)),
                ('facility', models.ManyToManyField(to='main.Facility')),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Reservation')),
            ],
            options={
                'permissions': (('can_view_room', 'Can view room'),),
                'ordering': ['room_no'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
            ],
            options={
                'permissions': (('can_view_staff', 'Can view staff'), ('can_view_staff_detail', 'Can view staff detail')),
                'ordering': ['first_name', 'middle_name', 'last_name'],
            },
        ),
    ]
