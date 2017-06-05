# from django import forms
# from models import Sign_Up_Data


# class Sign_Up_DataForm(forms.ModelForm):

# 	password = forms.CharField(widget=forms.PasswordInput)
# 	class Meta:
# 		model = Sign_Up_Data
# 		fields = ('username', 'email', 'number', 'country', 'password')

# class LoginForm(forms.ModelForm):

# 	password = forms.CharField(widget=forms.PasswordInput)

# 	class Meta:
# 		model = Sign_Up_Data
# 		fields = ('username', 'password')
# class MainForm(forms.Form):
# 	adult_num = forms.IntegerField(label='adult_num', )
# 	kid_num = forms.IntegerField(label='kid_num', )

from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'password']
		help_texts = {
            'username': None,
        }
