from __future__ import unicode_literals

from django.db import models

class States(models.Model):

	class Meta:
		db_table = "states"

	state_name = models.CharField(max_length=50,unique=True)
 

