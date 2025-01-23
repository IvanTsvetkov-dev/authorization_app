from django import forms

class RegistrationForm(forms.Form):
    login = forms.CharField(label="login", max_length=128)
    email = forms.EmailField(label="email")
    password = forms.CharField(label="passsword", widget=forms.PasswordInput)