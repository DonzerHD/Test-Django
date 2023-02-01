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
    active = models.BooleanField(default=True)
    year_formed = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    officiel_website = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=100, choices=Genre.choices, default=Genre.OTHER)

class Listing(models.Model):
    class Type(models.TextChoices):
        Record = 'Record'
        CD = 'CD'
        CLothing = 'Clothing'
        Other = 'Other'
        Poster = 'Poster'
        

    title = models.CharField(max_length=100)
    Nosold = models.BooleanField(default=True)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)], null=True, blank=True)
    types = models.CharField(max_length=100, choices=Type.choices, default=Type.Other)
    

    
