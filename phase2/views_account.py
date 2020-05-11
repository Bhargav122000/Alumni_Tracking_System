# this file includes account related functionalities like- login,register,logout,remove account (phase2)

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from . import models
from .models import *
from phase1.models import *
from datetime import date
import datetime

# function to the url - 'login_p2'
# functionality - for sign in of Institution (phase2)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username.find('@engg.clg')>0 or username.find('@engg.uni')>0 or username.find('@medi.clg')>0 or username.find('@medi.uni')>0 or username.find('@oth.clg')>0 or username.find('@oth.uni')>0 :
            user = auth.authenticate(username=username , password=password)
            if user is not None:
                auth.login(request, user)
                print("user logged-in")
                return redirect('home_p2')
            else:
                print("user not logged-in")
                return redirect('login_p2')
        else:
            return redirect('login_p2')
    else:
        states = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        return render(request,'phase2/login.html',{'states':states})

# function to the url - 'register_p2'
# functionality - for sign up of Institution (phase2)
def register(request):
    username = request.POST['username']
    inst_name = request.POST['inst_name']
    inst_field = request.POST['inst_field']
    inst_type = request.POST['inst_type']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email1']
    email2 = request.POST['email2']
    state = request.POST['state']
    place = request.POST['place']
    pincode = request.POST['pincode']

    if inst_field=='Engineering':
        if inst_type=='College':
            if username.find('@engg.clg') < 0:
                return redirect('login_p2')
        elif inst_type=='University':
            if username.find('@engg.uni') < 0:
                return redirect('login_p2')
    elif inst_field=='Medical':
        if inst_type=='College':
            if username.find('@medi.clg') < 0:
                return redirect('login_p2')
        elif inst_type=='University':
            if username.find('@medi.uni') < 0:
                return redirect('login_p2')
    elif inst_field=='Other':
        if inst_type=='College':
            if username.find('@oth.clg') < 0:
                return redirect('login_p2')
        elif inst_type=='University':
            if username.find('@oth.uni') < 0:
                return redirect('login_p2')

    if password1 == password2:
        if User.objects.filter(username=username).exists():
            print('Username already exists')
            return redirect('login_p2')
        elif User.objects.filter(email=email).exists():
            print('email already exists')
            return redirect('login_p2')
        else:
            user = User.objects.create_user(username=username,first_name='',last_name='',email=email,password=password1)
            user.save()
            obj = Institution(username = username,institution_name = inst_name,institution_field = inst_field,institution_type = inst_type,alt_email = email2,institution_state = state,institution_place = place,institution_pincode = pincode)
            obj.save()
            print('user created')
            return redirect('login_p2')
    else:
        print('password is not matching')
        return redirect('login_p2')
    return render(request,'phase2/login.html')

# function to the url - 'logout_p2'
# functionality - for logged-in Institution to logout (phase2)
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login_p2')

# function to the url - 'remove_p2'
# functionality - for deleting the Institution account (phase2)
def remove(request):
    if request.user.is_authenticated:
        username = request.user.username
        obj1 = Institution.objects.get(username=username)
        obj2 = User.objects.get(username=username)
        username = request.user.username
        if obj1.institution_field == 'Engineering':
            if obj1.institution_type == 'College':
                objs = EnggClg_Alumni.objects.filter(institution_name=obj1.institution_name)
            elif obj1.institution_type == 'University':
                objs = EnggUni_Alumni.objects.filter(institution_name=obj1.institution_name)
        elif obj1.institution_field == 'Medical':
            if obj1.institution_type == 'College':
                objs = MediClg_Alumni.objects.filter(institution_name=obj1.institution_name)
            elif obj1.institution_type == 'University':
                objs = MediUni_Alumni.objects.filter(institution_name=obj1.institution_name)
        elif obj1.institution_field == 'Other':
            if obj1.institution_type == 'College':
                objs = OthClg_Alumni.objects.filter(institution_name=obj1.institution_name)
            elif obj1.institution_type == 'University':
                objs = OthUni_Alumni.objects.filter(institution_name=obj1.institution_name)

        objs_l = list(objs)
        if len(objs_l)>0 :
            for obj in objs_l:
                obj.delete()

        events_obj = list(Event.objects.filter(name=obj1.institution_name))
        if len(events_obj)>0:
            for event_obj in events_obj:
                event_obj.delete()

        obj1.delete()
        auth.logout(request)
        obj2.delete()
        return redirect('login_p2')
    return redirect('login_p2')
