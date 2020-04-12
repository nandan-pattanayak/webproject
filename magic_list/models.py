from django.db import models

# Create your models here.
class Record(models.Model):
	search=models.TextField(max_length=500)
	datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.search)

