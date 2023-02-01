# Generated by Django 4.1 on 2023-02-01 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='types',
            field=models.CharField(choices=[('Record', 'Record'), ('CD', 'Cd'), ('Clothing', 'Clothing'), ('Other', 'Other'), ('Poster', 'Poster')], default='Other', max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]
