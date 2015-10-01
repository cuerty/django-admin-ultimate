#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Cousine, Recipe, Step


admin.site.register(Cousine)

admin.site.register(Recipe)

admin.site.register(Step)
