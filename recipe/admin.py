#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from django.conf.urls import patterns
from django.contrib import admin
from django.shortcuts import render

from .forms import RecipeForm
from .models import Cousine, Recipe, Step


logger = logging.getLogger(__name__)


@admin.register(Cousine)
class CousineAdmin(admin.ModelAdmin):
    fields = ('continent', 'name')


def make_french(modeladmin, request, queryset):
    french, created = Cousine.objects.get_or_create(name='French', defaults={'continent': 'eu'})
    queryset.update(cousine=french)

make_french.short_description = 'Make the selected recipes all french.'


class StepInline(admin.TabularInline):
    model = Step


class InitialsListFilter(admin.SimpleListFilter):
    title = 'recipe name initials'
    parameter_name = 'initials'

    def lookups(self, request, model_admin):
        return (
            ('F', 'F'),
            ('others', 'Others'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'F':
            return queryset.filter(name__startswith='F')
        return queryset


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('cousine', 'name', 'splash_image', 'ingredients_image')
    actions = [make_french]
    inlines = (StepInline,)
    list_filter = (InitialsListFilter,)
    list_display = ('name', 'get_thumbnail',)

    def get_urls(self):
        urls = super(RecipeAdmin, self).get_urls()
        return patterns('', (r'(\d+)/splash_images/$', self.admin_site.admin_view(self.splash_images)),) + urls

    def splash_images(self, request, recipe_id):
        recipe = Recipe.objects.get(pk=recipe_id)
        return render(request, 'splash_images.html', {'recipe': recipe})

    class Media:
        js = ('recipe_admin.js',)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = RecipeForm
            return super(RecipeAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        logger.info('%s modified recipe %s.' % (request.user.username, obj.name))
        obj.save()

    def delete_model(self, request, obj):
        logger.warning('%s deleted recipe %s.' % (request.user.username, obj.name))
        obj.save()
