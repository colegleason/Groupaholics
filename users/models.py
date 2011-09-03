from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Profile.objects.all().filter(profiletag__title='python')[0].user.username
class Profile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField()
	skill_tags = models.ManyToManyField('SkillTag')
	
CATEGORY_CHOICES = (
	(0, 'Project'),
	(1, 'Organization')
)
class Project(models.Model):
	description = models.TextField()
	tags = models.ManyToManyField('Tag')
	skill_tags = models.ManyToManyField('SkillTag')
	members = models.ManyToManyField('Profile', related_name='member_of')
	admins = models.ManyToManyField('Profile', related_name='admin_of')
	category = models.IntegerField(choices=CATEGORY_CHOICES)
	parent_project = models.ForeignKey('Project', null=True, blank=True)
	
class NewsEntry(models.Model):
	pub_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey('Profile')
	title = models.CharField(max_length=100)
	body = models.TextField()

class Tag(models.Model):
	title = models.CharField(max_length=20)
	
class SkillTag(models.Model):
	title = models.CharField(max_length=20)
	level = models.PositiveIntegerField()	
	
