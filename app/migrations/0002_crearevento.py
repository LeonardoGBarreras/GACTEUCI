# Generated by Django 4.1.3 on 2022-12-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrearEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
                ('requisitos', models.TextField()),
                ('transporte', models.BooleanField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]
