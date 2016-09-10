from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    passCheck = forms.CharField(label="Confirm password")
    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label="Last name")
    email = forms.EmailField(label="email")

    
