from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        ROCK = 'Rock'
        POP = 'Pop'
        METAL = 'Metal'
        JAZZ = 'Jazz'
        BLUES = 'Blues'
        COUNTRY = 'Country'
        CLASSICAL = 'Classical'
        FOLK = 'Folk'
        ELECTRONIC = 'Electronic'
        HIP_HOP = 'Hip Hop'
        REGGAE = 'Reggae'
        RAP = 'Rap'
        SOUL = 'Soul'
        DISCO = 'Disco'
        PUNK = 'Punk'
        INDIE = 'Indie'
        RNB = 'R&B'
        OTHER = 'Other'

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    active = models.BooleanField(default=True)
    officiel_website = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=100, choices=Genre.choices, default=Genre.OTHER)
    
class Listing(models.Model):
    title = models.CharField(max_length=100)