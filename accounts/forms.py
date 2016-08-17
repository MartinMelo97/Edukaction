from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repeat your Password", widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cp = self.cleaned_data
		if cp['password'] != cp['password2']:
			raise forms.ValidationError('The passwords do not match')
		return cp['password2']
			