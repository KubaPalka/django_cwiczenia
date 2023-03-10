# Generated by Django 4.1.7 on 2023-03-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('year', models.DateField()),
                ('still_active', models.BooleanField(default=True)),
                ('genre', models.IntegerField(choices=[(-1, 'Not defined'), (0, 'rock'), (1, 'metal'), (2, 'pop'), (3, 'hip-hop'), (4, 'electronic'), (5, 'reggae'), (6, 'other')], default=-1)),
            ],
        ),
    ]
