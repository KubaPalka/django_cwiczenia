# Generated by Django 4.1.7 on 2023-03-02 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bazy_danych', '0007_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bazy_danych.album'),
        ),
    ]
