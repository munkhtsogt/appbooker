from django.db import models

class Appointment(models.Model):
	date = models.CharField(max_length=10)
	time = models.CharField(max_length=10)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
 	def __str__(self):
		return self.date + " " + self.time
