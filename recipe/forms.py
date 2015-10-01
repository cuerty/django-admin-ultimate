#!/usr/bin/env python
# -*- coding: utf-8 -*-

import floppyforms.__future__ as forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Attributes from the form'}),
        }
        fields = ('cousine', 'name', 'splash_image', 'ingredients_image')
