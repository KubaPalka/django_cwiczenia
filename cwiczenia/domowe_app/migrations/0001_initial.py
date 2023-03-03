# Generated by Django 4.1.7 on 2023-03-02 17:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)])),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='domowe_app.person')),
                ('genre', models.ManyToManyField(to='domowe_app.genre')),
                ('screenplay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='domowe_app.person')),
                ('starring', models.ManyToManyField(to='domowe_app.person')),
            ],
        ),
    ]
