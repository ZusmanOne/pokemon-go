# Generated by Django 3.1.14 on 2022-05-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_pokemonelementtype_strong_against'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(blank=True, to='pokemon_entities.PokemonElementType', verbose_name='Силен против'),
        ),
    ]
