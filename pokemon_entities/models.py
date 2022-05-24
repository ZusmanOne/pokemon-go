from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название покемона')
    title_en = models.CharField(max_length=100,  blank=True, verbose_name='Английское название')
    title_jap = models.CharField(max_length=100,  blank=True, verbose_name='Японское название')
    image = models.ImageField(upload_to='image/%m/%d', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', default='описание покемона', blank=True)
    previous_evolution = models.ForeignKey('self',
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           verbose_name='Предыдущая версия покемона')

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name='Покемон',
                                related_name='pokemon_enities')
    appeared_at = models.DateTimeField(null=True, verbose_name='Время появления',)
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время исчезновения')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Урон')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

    class Meta:
        verbose_name = 'Сущность покемона'
        verbose_name_plural = 'Сущность покемонов'

    def __str__(self):
        return f'{self.pokemon}'
