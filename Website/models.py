from django.db import models

# Create your models here.
class Patient(models.Model):
	dayday = ''
	name = models.CharField(max_length=40)
	DayOfTheWeek = models.IntegerField(blank=True,null=True)
	session = models.IntegerField(blank=True,null=True)
	machine = models.IntegerField(blank=True,null=True)
	def __str__(self): 
         return f' {str(self.DayOfTheWeek)} {str(self.session)} {str(self.machine)} {str(self.name)}'
