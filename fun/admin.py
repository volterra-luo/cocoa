# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Tag, Joke

class JokeAdmin(admin.ModelAdmin):
	pass

admin.site.register(Joke, JokeAdmin)
