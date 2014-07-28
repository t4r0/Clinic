'''
Created on 27/07/2014

@author: t4r0
'''
from django import forms
from django.contrib.auth.models import User
from profiles.models import profile as Profile
class SignUpForm(forms.ModelForm):
    registration_number = forms.RegexField(label='Numero de colegiado',max_length=10,regex=r'[0-9]+$',help_text='Su numero de colegiado sin comas')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username',)
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile(user=user)
            profile.registration_number = self.cleaned_data['registration_number']
            profile.save()
        return user
        