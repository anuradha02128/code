# Generated by Django 4.1.4 on 2022-12-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('max_temp', models.CharField(max_length=50)),
                ('min_temp', models.CharField(max_length=50)),
                ('amt_precipitation', models.IntegerField()),
            ],
            options={
                'db_table': 'weather',
            },
        ),
        migrations.CreateModel(
            name='Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('tot_harvested', models.IntegerField()),
            ],
            options={
                'db_table': 'yield',
            },
        ),
    ]
