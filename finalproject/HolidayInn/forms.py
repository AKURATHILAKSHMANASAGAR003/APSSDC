from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from HolidayInn.models import Exfd,Room

class Usregis(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]
		widgets = {
		"first_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your First Name",	
			"required":True,		
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Last Name",	
			"required":True,		
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your EmailID",	
			"required":True,		
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your User Name",	
			"required":True,		
			}),
		}


class Upd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",		
			}),
		"first_name":forms.TextInput(attrs = {
			"class":"form-control",		
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Last Name",	
			"required":True,		
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",	
			}),
		}


class Pad(forms.ModelForm):
	class Meta:
		model = Exfd
		fields = ["age","gender","impf"]
		widgets = {
		"age":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Update your Age"
			}),
		"gender":forms.Select(attrs = {
			"class":"form-control",	
			}),
		}

class Rms(forms.ModelForm):
	class Meta:
		model = Room
		fields = ["category","Check_in","Check_out","capacity","beds"]
		widgets = {
		"category":forms.Select(attrs = {
			"class":"form-control",	
			"placeholder":"Select Room"
			}),
		"Check_in":forms.DateInput(attrs = {
			"class":"form-control",	
			"type":"date",
			"placeholder":"Check In",
			}),
		"Check_out":forms.DateInput(attrs = {
			"class":"form-control",	
			"placeholder":"Check Out",
			"type":"date",
			}),
		"capacity":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Number of People"
			}),
		"beds":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Number of Beds"
			}),
		}