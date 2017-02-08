# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-08 15:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile_no', models.CharField(default='+91', max_length=20)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2017, 2, 8, 15, 42, 46, 401419, tzinfo=utc))),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10)),
                ('profilePic', models.FileField(default='img/avatar5.png', upload_to='profile/')),
                ('verificationCode', models.CharField(default='zxsaqw', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('account', models.ManyToManyField(to='mysite.Account')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.CharField(choices=[('In', 'InRange'), ('Out', 'OutOfRange')], default='In', max_length=50)),
                ('battery_state', models.IntegerField(blank=True)),
                ('raw_gps', models.TextField(blank=True)),
                ('latitude', models.CharField(blank=True, max_length=150)),
                ('longitude', models.CharField(blank=True, max_length=150)),
                ('status', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='Online', max_length=50)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2017, 2, 8, 15, 42, 46, 404754, tzinfo=utc))),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(blank=True, max_length=500)),
                ('lng', models.CharField(blank=True, max_length=500)),
                ('speed', models.CharField(blank=True, max_length=500)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('deviceId', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Mqtt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('topic', models.CharField(default=' ', max_length=180)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
