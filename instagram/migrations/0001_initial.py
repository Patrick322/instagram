# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-09 07:42
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_pic', models.ImageField(upload_to=b'photos/')),
                ('caption', models.CharField(max_length=2000)),
                ('likes', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(null=True, upload_to=b'photos/')),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=50, null=True, verbose_name=django.contrib.auth.models.User)),
                ('bio', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='upload_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
