#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


class Cousine(models.Model):
    CONTINENT_CHOICES = (
        ('eu', 'Europe'),
        ('am', 'America'),
        ('af', 'Africa'),
    )

    continent = models.CharField('Continent', max_length=2, choices=CONTINENT_CHOICES, help_text='Continent where this cousine belongs to')
    name = models.CharField('Name', max_length=255, help_text='Name of the cousine')

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    cousine = models.ForeignKey(Cousine)
    name = models.CharField('Name', max_length=255, help_text='Name of the recipe')
    splash_image = ThumbnailerImageField('splash image', upload_to='splash/', help_text='Main image to display with the recipe')
    ingredients_image = ThumbnailerImageField('ingredients image', upload_to='ingredients/', help_text='Image to display simulating a cutting board')

    def get_thumbnail(self):
        return '<a href="/admin/recipe/recipe/%d/splash_images/"><img src="%s" /></a>' % (self.id, self.splash_image['50x50'].url)
    get_thumbnail.short_description = 'Thubmnail'
    get_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.name


class Step(models.Model):
    recipe = models.ForeignKey(Recipe)
    position = models.PositiveIntegerField('position', help_text='Position of this step in the recipe')
    image = ThumbnailerImageField('image', upload_to='step/', help_text='Image of the step')
    body = models.TextField('body', help_text='Step body text')

    class Meta:
        ordering = ('position',)
        unique_together = (('recipe', 'position'),)
