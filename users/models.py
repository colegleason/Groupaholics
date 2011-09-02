from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Profile.objects.all().filter(profiletag__title='python')[0].user.username
class Profile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField()
	
class Tag(models.Model):
	title = models.CharField(max_length=20)
	level = models.PositiveIntegerField()	
	
class ProfileTag(Tag):
	profile = models.ForeignKey('Profile')
	
