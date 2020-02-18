from django.db import models

# Create your models here.

class menu_item(models.Model):
	"""docstring for menu_item"""
	description=models.CharField(max_length=1000,null=True)
	image_present=models.BooleanField()
	large_portion_name=models.CharField(max_length=30,default="",null=True)
	name=models.CharField(max_length=100,default="")
	price_large=models.FloatField(null=True)
	price_small=models.FloatField(null=True)
	short_name=models.CharField(max_length=10,default="",null=True)
	small_portion_name=models.CharField(max_length=10,default="",null=True)