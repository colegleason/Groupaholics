from django import forms
from users.models import Profile, Project, Tag, SkillTag
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile

class RegForm(UserCreationForm):
	def isValidUsername(self, field_data, all_data): 
		try: 
			Profile.objects.get(username=field_data) 
		except Profile.DoesNotExist: 
			return 
		raise validators.ValidationError, _('A user with that username already exists.') 

	def save(self, new_data): 
		"Creates the user." 
		return Profile.objects.create_user(new_data['username'], '', new_data['password1']) 

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project

class Tag(forms.ModelForm):
	class Meta:
		model = Tag

class SkillTag(forms.ModelForm):
	class Meta:
		model = SkillTag
