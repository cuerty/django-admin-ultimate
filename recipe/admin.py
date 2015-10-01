#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Coucine, Recipe, Step


admin.site.register(Coucine)

admin.site.register(Recipe)

admin.site.register(Step)
