# Generated by Django 4.1.7 on 2023-10-08 16:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_picture_url', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='rrapp.user'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Rentee',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='rrapp.user'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023,
                            10,
                            8,
                            16,
                            48,
                            21,
                            329549,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                ('status', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('monthly_rent', models.IntegerField(default=1000)),
                (
                    'date_available_from',
                    models.DateField(default=datetime.date(2023, 10, 8)),
                ),
                (
                    'date_available_to',
                    models.DateField(default=datetime.date(2023, 11, 7)),
                ),
                (
                    'property_type',
                    models.CharField(
                        choices=[
                            ('independent_house', 'Independent house'),
                            ('apartment', 'Apartment'),
                        ],
                        default='apartment',
                        max_length=20,
                    ),
                ),
                (
                    'room_type',
                    models.CharField(
                        choices=[('private', 'Private'), ('shared', 'Shared')],
                        default='private',
                        max_length=20,
                    ),
                ),
                ('number_of_bedrooms', models.IntegerField(default=1)),
                ('number_of_bathrooms', models.IntegerField(default=1)),
                ('furnished', models.BooleanField(default=True)),
                ('utilities_included', models.BooleanField(default=True)),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='rrapp.user'
                    ),
                ),
            ],
        ),
    ]
