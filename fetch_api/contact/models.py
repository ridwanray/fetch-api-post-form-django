from django.db import models

#from django.db import models

class Contact(models.Model):
	name=models.CharField(max_length=200, blank=True, null=True)
	email=models.CharField(max_length=20, blank=True, null=True)
	subject=models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name
