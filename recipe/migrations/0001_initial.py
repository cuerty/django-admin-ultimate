# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coucine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('continent', models.CharField(help_text=b'Continent where this coucine belongs to', max_length=2, verbose_name=b'Continent', choices=[(b'eu', b'Europe'), (b'am', b'America'), (b'af', b'Africa')])),
                ('name', models.CharField(help_text=b'Name of the coucine', max_length=255, verbose_name=b'Name')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of the recipe', max_length=255, verbose_name=b'Name')),
                ('splash_image', easy_thumbnails.fields.ThumbnailerImageField(help_text=b'Main image to display with the recipe', upload_to=b'splash/', verbose_name=b'splash image')),
                ('ingredients_image', easy_thumbnails.fields.ThumbnailerImageField(help_text=b'Image to display simulating a cutting board', upload_to=b'ingredients/', verbose_name=b'ingredients image')),
                ('coucine', models.ForeignKey(to='recipe.Coucine')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveIntegerField(help_text=b'Position of this step in the recipe', verbose_name=b'position')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(help_text=b'Image of the step', upload_to=b'step/', verbose_name=b'image')),
                ('body', models.TextField(help_text=b'Step body text', verbose_name=b'body')),
                ('recipe', models.ForeignKey(to='recipe.Recipe')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='step',
            unique_together=set([('recipe', 'position')]),
        ),
    ]
