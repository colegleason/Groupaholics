from django import forms
from users.models import Profile, Project, Tag, SkillTag
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email


class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name',
			  'email', 'photo', 'bio')

class ProfileCreationForm(UserCreationForm): 
	class Meta:
		model = Profile
		fields = ("username", "email")

	def clean_username(self):
       		username = self.cleaned_data["username"]
		try:
			Profile.objects.get(username=username)
		except Profile.DoesNotExist:
			return username
		raise forms.ValidationError("A user with that username already exists.")


	def save(self, commit=True):
		user = super(ProfileCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class ProjectForm (forms.ModelForm):
	class Meta:
		model = Project
		fields = ('name', 'description', 'tags', 'skill_tags', 'category')

class Tag(forms.ModelForm):
	class Meta:
		model = Tag

class SkillTag(forms.ModelForm):
	class Meta:
		model = SkillTag
