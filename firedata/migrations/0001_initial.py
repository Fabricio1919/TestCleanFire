# Generated by Django 5.1.2 on 2024-10-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipioQueimada',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('data_hora', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('bioma', models.CharField(max_length=100)),
                ('dias_sem_chuva', models.IntegerField()),
                ('precipita', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('frp', models.FloatField()),
            ],
        ),
    ]
