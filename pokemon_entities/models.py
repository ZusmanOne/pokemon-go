from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название покемона')
    image = models.ImageField(upload_to='image/%m/%d', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1, verbose_name='Покемон')
    appeared_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время появления',)
    disappeared_at = models.DateTimeField(null=True,verbose_name='Время исчезновения')
    level = models.IntegerField(null=True,verbose_name='Уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, verbose_name='Урон')
    defence = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='Выносливость')

# your models here
