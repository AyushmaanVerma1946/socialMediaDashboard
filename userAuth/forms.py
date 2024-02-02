from typing import Any
from  django import forms
from django.contrib.auth.models import User

class registerForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        
    def save(self, commit: bool = ...) -> Any:
        data = super()
        data = data.__dict__['cleaned_data']
        user = User.objects.create(**data)
        user.set_password(data['password'])
        user.save()
        return user
        
        
    
class loginForm(forms.Form):  
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class profileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            "username",
            'first_name',
            'last_name',
            'email',
            'last_login'            
        ]