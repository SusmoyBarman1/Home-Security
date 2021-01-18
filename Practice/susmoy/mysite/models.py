from django.db import models

# Create your models here.

class Work(models.Model):
	# adding database model column
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	img = models.ImageField(upload_to='pics')
	caption = models.TextField()
	offer = models.BooleanField(default=False)