from django.db import models

class Appointment(models.Model):
	datetime = models.DateTimeField(null=True, blank=True)
	desc = models.CharField(max_length=255)
	
 	def __str__(self):
		return str(self.datetime.strftime("%Y-%m-%d %H:%M"))
