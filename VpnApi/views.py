from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import LoginForm , VpnForm , AddAppForm
from .models import VpnModel ,CountryModel , ApplicationModel




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

def appdashboard_view(request ):

    allvpn = VpnModel.objects.all()
    allapps = ApplicationModel.objects.all()
    forms = AddAppForm()

    if request.method == 'POST':
        # applogo = request.FILES['applogo'].read()
        # appname = request.POST.get('appname')
        # packagename = request.POST.get('packagename')
        # vpnserver = request.POST.get('vpnserver')
        # print(applogo)
        # print(appname)
        # print(packagename)
        # print(vpnserver)

        forms = AddAppForm(request.POST , request.FILES)
        if forms.is_valid():
            forms.save()

            return redirect('appdashboard')
        
        else:
            print('form validation fails')

    context = {'allvpn' : allvpn , 'allapps' : allapps , 'forms':forms}
    return render(request , 'appdashboard.html' , context)
