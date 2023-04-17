from rest_framework import serializers
from .models import ApplicationModel


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ['id' ,'applogo', 'appname' , 'packagename' , 'vpnserver']


        

