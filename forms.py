from django import forms
from users.models import Profile, Project, Tag, SkillTag
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project

class Tag(forms.ModelForm):
	class Meta:
		model = Tag

class SkillTag(forms.ModelForm):
	class Meta:
		model = SkillTag
