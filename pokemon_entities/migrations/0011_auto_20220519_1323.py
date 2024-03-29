# Generated by Django 3.1.14 on 2022-05-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_pokemon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Английское название'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jap',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Японское название'),
        ),
    ]
