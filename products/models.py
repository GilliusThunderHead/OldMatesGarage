from django.db import models
import time
from datetime import date
from django.contrib.auth.models import User


# Product Class
class Product(models.Model):

	title=models.CharField(max_length=50)
	url=models.TextField()
	pub_date=models.DateTimeField()
	votes_total=models.IntegerField(default=1)
	image=models.ImageField(upload_to='images/')
	icon=models.ImageField(upload_to='images/')
	video=models.FileField(upload_to='videos/',default=1)
	body=models.TextField()
	#pub_date_pretty=models.DateTimeField()
	hunter=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		
	def summary(self):
		return self.body[:200]
			
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %y')