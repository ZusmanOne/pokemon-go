import folium
from django.utils.timezone import localtime
from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = PokemonEntity.objects.filter(appeared_at__lte=localtime(), disappeared_at__gte=localtime())
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            request.build_absolute_uri(pokemon.pokemon.image.url)
        )
    pokemons_on_page = Pokemon.objects.all()
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    my_pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon_id=my_pokemon.pk, appeared_at__lte=localtime(),
                                                       disappeared_at__gte=localtime()):
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(my_pokemon.image.url)
        )
    serialized_pokemon = {}
    for pokemon in Pokemon.objects.filter(pk=pokemon_id):
        pokemons = []
        pokemons.append({
            'pokemon_id': pokemon.pk,
            'title_ru': pokemon.title,
            'title_en': pokemon.title_en,
            'title_jp': pokemon.title_jap,
            'entities': [{
                'lan': entity.lat,
                'lon': entity.lon,
            } for entity in PokemonEntity.objects.filter(pokemon_id=pokemon.pk)],

        })
        serialized_pokemon['pokemons'] = pokemons
        if pokemon.next_evolutions:
            next_evolution = {}
            for next_pokemon in pokemon.next_evolutions.all():
                next_evolution['title_ru'] = next_pokemon.title
                next_evolution['pokemon_id'] = next_pokemon.id
                next_evolution['img_url'] = next_pokemon.image.url
            serialized_pokemon['pokemons'][0]['next_evolution'] = next_evolution

        if pokemon.previous_evolution:
            previous_evolution = {
                'title': pokemon.previous_evolution.title,
                'pokemon_id': pokemon.previous_evolution.id,
                'img_url': pokemon.previous_evolution.image.url,
            }
            serialized_pokemon['pokemons'][0]['previous_evolution'] = previous_evolution

    print(serialized_pokemon)
    pokemon_next = my_pokemon.next_evolutions.all()
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': my_pokemon, 'pokemon_next': pokemon_next,
    })
