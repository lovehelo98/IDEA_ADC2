from django import forms 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class NewForm(UserCreationForm):
    email = forms.EmailField(required=True)
    ideaPeacher_or_Sponsor = forms.CharField(max_length=100,required=True)  
    class Meta:
        model = User
        fields = ['username', 'email','ideaPeacher_or_Sponsor', 'password1','password2']

    def save(self, commit=True):
        user = super(NewForm , self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.ideaPeacher_or_Sponsor = self.cleaned_data['ideaPeacher_or_Sponsor']

        if commit:
            user.save()

        return user
