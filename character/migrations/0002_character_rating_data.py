# Generated by Django 3.1.2 on 2020-10-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='rating_data',
            field=models.JSONField(default={'rates_sum': 0, 'times_rated': 0}),
        ),
    ]