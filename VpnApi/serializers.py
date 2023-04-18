from rest_framework import serializers
from .models import ApplicationModel , VpnModel


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ['id' ,'applogo', 'appname' , 'packagename' , 'vpnserver']


class VpnSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnModel
        fields = ['id' ,'hostname', 'countryshorts' , 'username' , 'pasword' , 'config' , 'config']



        

