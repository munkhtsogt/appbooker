from django.db import models

class Appointment(models.Model):
	datetime = models.DateTimeField(null=True, blank=True)
	description = models.TextField()
	
 	def __str__(self):
		return str(self.datetime) + " " + str(self.description)
