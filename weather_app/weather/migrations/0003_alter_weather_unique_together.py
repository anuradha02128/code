# Generated by Django 4.1.4 on 2022-12-28 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_weather_amt_precipitation_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='weather',
            unique_together={('date', 'max_temp', 'min_temp', 'amt_precipitation')},
        ),
    ]
