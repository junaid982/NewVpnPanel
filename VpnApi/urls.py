from django.urls import path
from . import views



urlpatterns = [
    path('update-vpn-server/<int:id>/' , views.UpdateVpnServer_api),
    path('allvpn/' , views.allvpn_api),  # all vpn enable data
    path('all-vpn/' , views.allvpns_api),  # all vpn enable data 
    # path('all-activevpn/' , views.activevpn_api),  # all Active vpn enable data 
    # path('all-deactivevpn/' , views.allvpns_api),  # all all deactive vpn enable data 



]