from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	impf = models.ImageField(upload_to="Profile/",default="profile.jpg")

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)

class Room(models.Model):
	ROOM_CATEGORIES = [
	('DEL','DELUXE'),
	('NDL','NON-DELUXE'),
	]
	category = models.CharField(max_length=3,choices=ROOM_CATEGORIES)
	capacity = models.IntegerField()
	beds = models.IntegerField()
	Check_in = models.DateField()
	Check_out = models.DateField()
	m = models.ForeignKey(User,on_delete=models.CASCADE)