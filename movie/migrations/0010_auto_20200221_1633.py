# Generated by Django 3.0.3 on 2020-02-21 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_movie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]