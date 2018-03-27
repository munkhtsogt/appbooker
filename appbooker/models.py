from django.db import models

class Appointment(models.Model):
	date = models.DateField()
	time = models.TimeField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
 	def __str__(self):
		return str(self.date) + " " + str(self.time)
