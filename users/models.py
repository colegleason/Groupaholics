from django.db import models
from django.contrib.auth.models import User
from django.utils import unittest

# Create your models here.

#Profile.objects.all().filter(profiletag__title='python')[0].user.username
class Profile(User):
	photo = models.ImageField(upload_to='/profile_pics', blank=True, default='/medi/no-photo-25.png')
	bio = models.TextField(blank=True, null=True, default='')
	skill_tags = models.ManyToManyField('SkillTag', blank=True, null=True)
	projects = models.ManyToManyField('Project', blank=True, null=True)
	
CATEGORY_CHOICES = (
	(0, 'Project'),
	(1, 'Organization')
)

class Project(models.Model):
	name = models.TextField(max_length=100)
	description = models.TextField(blank=True)
	tags = models.ManyToManyField('Tag', blank=True)
	skill_tags = models.ManyToManyField('SkillTag', blank=True)
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
	
class ProjectProfileTest(unittest.TestCase):
	def setUp(self):
		self.cTag = SkillTag(title='c', level=3)
		self.cppTag = SkillTag(title='c++', level=2)
		self.javaTag = SkillTag(title='java', level=2)
		self.phpTag = SkillTag(title='php', level=2)
		self.pythonTag = SkillTag(title='python', level=3)
		self.zach = Profile(username='zach297', bio='Senior Cool Kid')
		self.zach.save()
		for tag in [self.cTag, self.cppTag, self.javaTag, self.phpTag, self.pythonTag]:
			tag.save()
			self.zach.skill_tags.add(tag)
			
		self.bob = Profile(username='bob', bio='Kinda Generic')
		self.bob.save()
		self.bob.skill_tags.add(self.javaTag)
		self.bob.skill_tags.add(self.pythonTag)
					
	def test_tag_search(self):
		self.assertEqual(len(Profile.objects.filter(skill_tags__title='python', skill_tags__level__gt=1)), 2)
		self.assertEqual(Profile.objects.filter(skill_tags__title='python', skill_tags__level__gt=1).filter(skill_tags__title='c')[0], self.zach)
