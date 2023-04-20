from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import LoginForm , VpnForm , AddAppForm
from .models import VpnModel ,CountryModel , ApplicationModel
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

from .serializers import AppSerializer , VpnSerializer



# api views
@api_view(['PUT'])
def UpdateVpnServer_api(request , id):

    if request.method == 'PUT':
        print(id)

        # fetching old app data as per id 
        appdata = ApplicationModel.objects.get(id = id)

        # accept data from request
        newdata = request.data
        print(newdata)
        print(type(newdata))


        # call serializer to update 
        # serializer = StudentSerializer(stu, data=pythondata, partial=True)
        serializer = AppSerializer(appdata, data=newdata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':'Server Updated Successfully '} , safe=False)

        return JsonResponse(serializer.errors , safe=False)

        # return Response(serializer.data)
    

# return all data enable or diable both 
@permission_classes((IsAuthenticated, ))
@api_view(['POST'])
def allvpn_api(request):
    if request.method =='POST':
        try:
            #get package name from request
            packagename = request.data['packagename']

            # check application exist or not from our side 
            allapp = ApplicationModel.objects.get(packagename = packagename)

            vpnserver = set(allapp.vpnserver.split(','))
            
            allvpn = VpnModel.objects.filter(countryshorts__in = vpnserver , is_enable = True)
            # allvpn = allvpn.filter()
            
            serializer = VpnSerializer(allvpn , many=True)

            return JsonResponse(serializer.data , safe=False )

        except:
            return JsonResponse({'status':'Package Not Found'} , safe=False )



@permission_classes((IsAuthenticated, ))
@api_view(['GET'])       
def allvpns_api(request):
    if request.method == "GET":

        allvpn = VpnModel.objects.all()
        active = request.GET.get('active')
        # print(active ,type(active))
        if active == 'true':
            activevpn = allvpn.filter(is_enable = True)
            serializer = VpnSerializer(activevpn , many=True)
            print("Response All Enable Vpn ")

            return JsonResponse(serializer.data , safe=False )

        # print(active ,type(active))
        if active == 'false ':
            deactivevpn = allvpn.filter(is_enable = False)
            serializer = VpnSerializer(deactivevpn , many=True)
            
            print("Response All Disable Vpn ")
            return JsonResponse(serializer.data , safe=False )

        serializer = VpnSerializer(allvpn , many=True)
        print("Response All Vpn ")
        return JsonResponse(serializer.data , safe=False )




# all activ vpn 
# @permission_classes((IsAuthenticated, ))
# @api_view(['GET'])
# def activevpn_api()



# Create your views here.




def notfound(request , exception):
    return render(request , 'pagenotfound.html')



def signin_view(request):

    if request.user.is_authenticated:
        return redirect('vpndashboard')

    forms = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        user = authenticate(username = username , password = password)
        # print(user)
        if user is not None :
            login(request , user)
            messages.info(request, 'Login Successfull')
            return redirect('vpndashboard')

            

        messages.info(request, 'Something Went Wrong Check Your Username or Password')

        
    context = {'forms':forms}
    return render(request , 'signin.html' , context)






# Logout View 
@login_required(login_url='signin')
def signout_view(request):

    messages.info(request, 'Logout Successfull')
    
    logout(request)
    return redirect('signin')



# Vpn dashboard View

@login_required(login_url='signin')
def vpndashboard_view(request):

    allvpn = VpnModel.objects.all()

    user = request.user
    context = {'user' : user , 'allvpn':allvpn}

    return render(request , 'vpndashbord.html' , context)




# add vpn  view
@login_required(login_url='signin')
def addvpn_view(request):
    
    countries = CountryModel.objects.all()
    forms = VpnForm()
    
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        countryshorts = request.POST.get('countryshorts')
        username = request.POST.get('username')
        pasword = request.POST.get('pasword')
        config = request.POST.get('config')

        # print(hostname)
        # print(countryshorts)
        # print(username)
        # print(pasword)
        # print(config)

        all_vpn = VpnModel(hostname = hostname , countryshorts = countryshorts , username = username , pasword = pasword ,config=config)
        all_vpn.save()

        return redirect('vpndashboard')

    context = {'forms' : forms ,'countries':countries}
    return render(request , 'addvpn.html' , context)




# delete vpn
@login_required(login_url='signin')
def deletevpn_view(request , id):

    allvpn = VpnModel.objects.get(id = id).delete()

    return redirect('vpndashboard')




# update Vpn 

@login_required(login_url='signin')
def updatevpn_view(request , id):

    countries = CountryModel.objects.all()
    vpn = VpnModel.objects.get(id = id)
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        countryshorts = request.POST.get('countryshorts')
        username = request.POST.get('username')
        pasword = request.POST.get('password')
        config = request.POST.get('config')
        is_enable = request.POST.get('is_enable')
        if is_enable == 'on':
            is_enable = True
        if is_enable == None:
            is_enable = False


        # print(hostname)
        # print(countryshorts)
        # print(username)
        # print(pasword)
        # print(config)
        # print(is_enable)
        vpn.hostname = hostname
        vpn.countryshorts = countryshorts
        vpn.username = username
        vpn.pasword = pasword
        vpn.config = config
        vpn.is_enable = is_enable
        vpn.save() 
        return redirect('vpndashboard')

    context = {'vpn' : vpn ,'countries':countries}
    return render(request , 'updatevpn.html' ,context) 



# application

# def appdashboard_view(request ):

#     allvpn = VpnModel.objects.all()
#     allapps = ApplicationModel.objects.all()
#     forms = AddAppForm()

#     if request.method == 'POST':
#         # applogo = request.FILES['applogo'].read()
#         # appname = request.POST.get('appname')
#         # packagename = request.POST.get('packagename')
#         # vpnserver = request.POST.get('vpnserver')
#         # print(applogo)
#         # print(appname)
#         # print(packagename)
#         # print(vpnserver)

#         forms = AddAppForm(request.POST , request.FILES)
#         if forms.is_valid():
#             forms.save()

#             return redirect('appdashboard')
        
#         else:
#             print('form validation fails')

#     context = {'allvpn' : allvpn , 'allapps' : allapps , 'forms':forms}
#     return render(request , 'appdashboard.html' , context)




@login_required(login_url='signin')
def appdashboard_view(request ):

    allvpn = VpnModel.objects.filter(is_enable = True)
    allapps = ApplicationModel.objects.all()
    forms = AddAppForm()
    # get all vpn region added into vpn panel
    allvpnregion = []
    for vpn in allvpn:
        if vpn.countryshorts not in allvpnregion:
            allvpnregion.append(vpn.countryshorts)

    # print("All vpn regions :",allvpnregion , '\n')
    # add apps 
    if request.method == 'POST':
        applogo = request.FILES.get('applogo')
        appname = request.POST.get('appname')
        packagename = request.POST.get('packagename')
        vpnserver = request.POST.get('vpnserver')

        print('Vpn Server ',vpnserver , '\n')
        print('len of vpn ',len(vpnserver) , '\n')
        # print(applogo , type(applogo))
        # print(appname)
        # print(packagename)
        # print(vpnserver , type(vpnserver))

        if vpnserver == "" or vpnserver == " ":
            
            vpnserver = ','.join(allvpnregion)
            # print('selected Vpn regions ', vpnserver, '\n')

        apps = ApplicationModel()
        apps.applogo = applogo
        apps.appname = appname
        apps.packagename = packagename
        print('Befor insert VPN ',vpnserver, '\n')
        apps.vpnserver = vpnserver
        apps.save()
        return redirect('appdashboard')

    
    context = {'allvpn' : allvpn , 'allapps' : allapps , 'forms':forms ,'allvpnregion':allvpnregion }
    return render(request , 'appdashboard.html' , context)



# delete app 
@login_required(login_url='signin')
def DeleteApp_view(request , id):

    apps = ApplicationModel.objects.get(id = id).delete()

    return redirect('appdashboard')


@login_required(login_url='signin')
def UpdateApp_view(request , id):
    app = ApplicationModel.objects.get(id = id)

    if request.method == 'POST':
        appname = request.POST.get('uappname')
        packagename = request.POST.get('upackagename')
        applogo = request.FILES.get('uapplogo')

        
        

        print(applogo)
        print(appname)
        print(packagename)
        # print(vpnserver)

        app.appname = appname
        app.packagename = packagename

        if applogo:
            app.applogo = applogo

        app.save()

        return redirect('appdashboard')




    context = {'app':app}
    return render(request , 'updateapp.html' , context)