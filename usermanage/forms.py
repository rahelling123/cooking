from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
