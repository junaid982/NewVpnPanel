from django.db import models
from django_countries.fields import CountryField
from django_countries import countries

# Create your models here.




class CountryModel(models.Model):
    shortName = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)




class VpnModel(models.Model):
    hostname = models.CharField(max_length=100)
    # contryshorts = models.ForeignKey(CountryModel ,on_delete=models.CASCADE)
    countryshorts = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    pasword = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_enable = models.BooleanField(default=True)
    config = models.TextField()

    def __str__(self):
        # return str(self.countryshorts)
        return self.countryshorts


class ApplicationModel(models.Model):
    applogo = models.ImageField(upload_to='ApplicationLogo/')
    appname = models.CharField(max_length=100)
    packagename = models.CharField(max_length=100)
    # vpnserver = models.ForeignKey(VpnModel , on_delete=models.CASCADE)
    vpnserver = models.CharField(max_length=250)