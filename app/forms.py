from django import forms


class Authentificaton(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control'
                             }),
                             required=True)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Password',
                                   'class': 'form-control'
                               }),
                               required=True)
