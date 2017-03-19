from django import forms

class MainForm(forms.Form):
	adult_num = forms.IntegerField(label='adult_num', )
	kid_num = forms.IntegerField(label='kid_num', )