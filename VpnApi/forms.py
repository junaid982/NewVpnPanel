
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from .models import VpnModel , ApplicationModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Enter Username' , widget=forms.TextInput(attrs={"class": 'form-control'}))
    password = forms.CharField(label = 'Enter Password' , widget=forms.PasswordInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ['username' , 'password']



class VpnForm(forms.ModelForm):

    # countryshorts= forms.CharField(label = 'Select Vpn Countryshorts',widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = VpnModel
        fields = ['hostname' , 'countryshorts' , 'username' , 'pasword'  , 'config']

        labels = {
        
            'hostname': 'Enter Hostname', 
            'countryshorts': 'Select Vpn Countryshorts',
            'username' : 'Enter Vpn Username', 
            'pasword' : 'Enter Vpn Password',
            'config' :'Enter Vpn Config' 
        }

        widgets = {
            'hostname': forms.TextInput(attrs={'class':'form-control'}), 
            'countryshorts': forms.Select(attrs={'class':'form-control'}),
            'username' :forms.TextInput(attrs={'class':'form-control'}), 
            'pasword' :forms.TextInput(attrs={'class':'form-control'}) ,
            'config' :forms.Textarea(attrs={'class':'form-control'}) 
        }



class AddAppForm(forms.ModelForm):

    class Meta:
        model = ApplicationModel
        fields = ['applogo' , 'appname' , 'packagename' , 'vpnserver']
        widgets = {
            'applogo': forms.FileInput(attrs={'class':'form-control'}), 
            
            'appname' :forms.TextInput(attrs={'class':'form-control'}), 
            'packagename' :forms.TextInput(attrs={'class':'form-control'}) ,
            'vpnserver' :forms.Select(attrs={'class':'form-control'}) 
        }