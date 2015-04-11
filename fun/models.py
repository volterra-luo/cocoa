from django.db import models
import uuid

class Tag(models.Model):
	name = models.CharField(max_length='20', primary_key=True)

class Joke(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length='30')
	content = models.TextField(blank=True)
	tags = models.ManyToManyField(Tag)
