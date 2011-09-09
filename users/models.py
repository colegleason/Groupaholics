from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Profile.objects.all().filter(profiletag__title='python')[0].user.username
class Profile(models.Model):
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='/profile_pics', blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	skill_tags = models.ManyToManyField('SkillTag', blank=True, null=True)
	projects = models.ManyToManyField('Project', blank=True, null=True)
	
CATEGORY_CHOICES = (
	(0, 'Project'),
	(1, 'Organization')
)

class Project(models.Model):
	name = models.TextField(max_length=100)
	description = models.TextField()
	tags = models.ManyToManyField('Tag')
	skill_tags = models.ManyToManyField('SkillTag')
	members = models.ManyToManyField('Profile', related_name='member_of')
	admins = models.ManyToManyField('Profile', related_name='admin_of')
	category = models.IntegerField(choices=CATEGORY_CHOICES)
	parent_project = models.ForeignKey('Project', null=True, blank=True)
	slug = models.SlugField(max_length=100)
	
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
	
