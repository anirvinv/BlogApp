from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class BlogForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)