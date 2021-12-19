from django.db import models
from .utils import from_cirillic_to_eng


class City(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Название населённого пункта')
    slug = models.CharField(max_length=65, blank=True, unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cirillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    
    name = models.CharField(max_length=50, unique=True, verbose_name='Язык программирования')
    slug = models.CharField(max_length=65, blank=True, unique=True)

    class Meta:
        verbose_name='Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cirillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):

    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описпние вакансии')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык программирования')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
