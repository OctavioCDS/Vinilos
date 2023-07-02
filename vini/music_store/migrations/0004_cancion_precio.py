# Generated by Django 4.2.1 on 2023-07-02 05:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0003_cancion_artistas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='precio',
            field=models.IntegerField(default=1000, validators=[django.core.validators.MinValueValidator(1000)]),
        ),
    ]
