# this file includes account related functionalities like- login,register,logout,remove account (phase1)

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from .models import *
from phase2.models import *
from django.conf import settings
import urllib.request
from os.path import realpath

# function to the url - 'login_p1'
# functionality - for sign in of Alumni member(phase1)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username.find('@engg.clg')>0 or username.find('@engg.uni')>0 or username.find('@medi.clg')>0 or username.find('@medi.uni')>0 or username.find('@oth.clg')>0 or username.find('@oth.uni')>0 :
            print('wrong format of username')
            return redirect('login_p1')
        else :
            user = auth.authenticate(username=username , password=password)
            if user is not None:
                auth.login(request, user)
                print("user logged-in")
                return redirect('home_p1')
            else:
                print("user not logged-in")
                return redirect('login_p1')
    else:
        return render(request,'phase1/login.html')

# function to the url - 'register_p1'
# functionality - for sign up of Alumni member (phase1)
def register(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if username.find('@engg.clg')>0 or username.find('@engg.uni')>0 or username.find('@medi.clg')>0 or username.find('@medi.uni')>0 or username.find('@oth.clg')>0 or username.find('@oth.uni')>0 :
        print('wrong format of username')
        return redirect('login_p1')

    if password1 == password2:
        if User.objects.filter(username=username).exists():
            print('Username already exists')
            return redirect('login_p1')
        elif User.objects.filter(email=email).exists():
            print('email already exists')
            return redirect('login_p1')
        else:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
            user.save()
            print('user created')
            return redirect('login_p1')
    else:
        print('password is not matching')
        return redirect('login_p1')

# function to the url - 'logout_p1'
# functionality - for logged-in Alumni member to logout (phase1)
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)   
    return redirect('login_p1')

# function to the url - 'remove_p1'
# functionality - for deleting the Alumni member account (phase1)
def remove(request):
    if request.user.is_authenticated:
        obj1 = None
        obj2 = None
        obj3 = None
        obj4 = None
        obj5 = None
        username = request.user.username
        name = request.user.first_name + " " + request.user.last_name
        email = request.user.email
        if Profile_personal.objects.filter(username=username).exists():
            obj1 = Profile_personal.objects.get(username=username)
            
        if Profile_highEdu.objects.filter(username=username).exists():
            obj2 = Profile_secEdu.objects.get(username=username)
            obj3 = Profile_hsecEdu.objects.get(username=username)
            obj4 = Profile_highEdu.objects.get(username=username)
        if Profile_pro.objects.filter(username=username).exists():
            obj5 = Profile_pro.objects.get(username=username)

        if obj4 is not None:
            if obj4.field == 'Engineering':
                if obj4.ofType == 'College':
                    if EnggClg_Alumni.objects.filter(person_name=name).filter(person_email=email).filter(institution_name=obj4.name).filter(institution_branch=obj4.branch).filter(institution_year_pass=obj4.year_pass).exists():
                        obj = EnggClg_Alumni.objects.get(person_email = email)
                        obj.delete()
                elif obj4.ofType == 'University':
                    if EnggUni_Alumni.objects.filter(person_name=name).filter(person_email=email).filter(institution_name=obj4.name).filter(institution_branch=obj4.branch).filter(institution_year_pass=obj4.year_pass).exists():
                        obj = EnggUni_Alumni.objects.get(person_email = email)
                        obj.delete()
            elif obj4.field == 'Medical':
                if obj4.ofType == 'College':
                    if MediClg_Alumni.objects.filter(person_name=name).filter(person_email=email).filter(institution_name=obj4.name).filter(institution_branch=obj4.branch).filter(institution_year_pass=obj4.year_pass).exists():
                        obj = MediClg_Alumni.objects.get(person_email = email)
                        obj.delete()
                elif obj4.ofType == 'University':
                    if MediUni_Alumni.objects.filter(person_name=name).filter(person_email=email).filter(institution_name=obj4.name).filter(institution_branch=obj4.branch).filter(institution_year_pass=obj4.year_pass).exists():
                        obj = MediUni_Alumni.objects.get(person_email = email)
                        obj.delete()
            elif obj4.field == 'Other':
                if obj4.ofType == 'College':
                    if OthClg_Alumni.objects.filter(person_name=name).filter(person_email=email).filter(institution_name=obj4.name).filter(institution_branch=obj4.branch).filter(institution_year_pass=obj4.year_pass).exists():
                        obj = OthClg_Alumni.objects.get(person_email = email)
                        obj.delete()
                elif obj4.ofType == 'University':
                    if OthUni_Alumni.objects.filter(person_name=name).filter(person_email=email).filter(institution_name=obj4.name).filter(institution_branch=obj4.branch).filter(institution_year_pass=obj4.year_pass).exists():
                        obj = OthUni_Alumni.objects.get(person_email = email)
                        obj.delete()

        events_obj = list(Event.objects.filter(name=name))
        if len(events_obj)>0:
            for event_obj in events_obj:
                event_obj.delete()

        if obj1 is not None :
            obj1.delete()
        if obj2 is not None :
            obj2.delete()
        if obj3 is not None :
            obj3.delete()
        if obj4 is not None :
            obj4.delete()
        if obj5 is not None :
            obj5.delete()
        obj = User.objects.get(username=username)
        auth.logout(request)
        obj.delete()
        return redirect('login_p1')
    else:
        return redirect('login_p1')
