from django.contrib import admin

from .models import  VpnModel , ApplicationModel , CountryModel

# Register your models here.


admin.site.register(CountryModel)
# admin.site.register(VpnModel)

@admin.register(VpnModel)
class VpnAdmin(admin.ModelAdmin):
    list_display = ['id' , 'hostname' , 'countryshorts' , 'username' , 'pasword' , 'created_at' , 'updated_at' , 'is_enable' , 'config']



@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id' , 'applogo' , 'appname' , 'packagename' , 'vpnserver']

