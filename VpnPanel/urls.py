"""
URL configuration for VpnPanel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from VpnApi import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.signin_view , name = 'signin'),  # for login page 
    path('vpndashboard/' , views.vpndashboard_view , name='vpndashboard'),  # vpn dashboard 
    path('signout/' , views.signout_view , name = 'signout'), # logout 

    path('addvpn/' , views.addvpn_view , name = 'addvpn'), # add vpn 
    path('deletevpn/<int:id>/' , views.deletevpn_view , name = 'deletevpn'), # Delete vpn
    path('updatevpn/<int:id>/' , views.updatevpn_view , name = 'updatevpn'), # Delete vpn 

    # application
    path('appdashboard/' , views.appdashboard_view , name='appdashboard'),  # vpn dashboard 




    # path('^.*', views.notfound ),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

