# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from django.contrib.postgres.fields import ArrayField


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)

	city = models.CharField(max_length=128)
	style = ArrayField(
		models.CharField(max_length=128),
		default=list
	)
	ratings = ArrayField(
		models.IntegerField(null=True, blank=True),
		default=list
	)
	description = models.CharField(max_length=2048)
	featured = models.BooleanField(default=False)
