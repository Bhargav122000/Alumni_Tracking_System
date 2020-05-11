# this file includes functionalities for displaying Alumni page of website (phase2)
# this file also includes functionalities for Institutions to view their alumni (by filtering or whole)
# this file also includes functionality for Institutions to accept or reject the requests of Individuals.

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from . import models
from .models import *
from datetime import date
from django.core.mail import send_mail,EmailMessage
from .views_home import month_history
from phase1.models import *
import datetime

# function to the url - 'alumni_p2'
# functionality - for displaying Alumni page of website (phase2)
def alumni(request):
    if request.user.is_authenticated:
        d = datetime.datetime.now()
        desc = month_history(d.month)
        link = "https://thisdayintechhistory.com/"+str(d.month)+"/"+str(d.day)+"/"
        month_dic = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        username = request.user.username
        obj = Institution.objects.get(username=username)
        if obj.institution_field == 'Engineering':
            if obj.institution_type == 'College':
                objs = EnggClg_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = EnggUni_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
        elif obj.institution_field == 'Medical':
            if obj.institution_type == 'College':
                objs = MediClg_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = MediUni_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
        elif obj.institution_field == 'Other':
            if obj.institution_type == 'College':
                objs = OthClg_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = OthUni_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)

        objs_l = list(objs)
        if len(objs_l)>0 :
            have_request = True
        else:
            have_request = False
        return render(request,'phase2/alumni.html',{'have_request':have_request,'day':d.day,'month':month_dic[d.month],'year':d.year,'week':d.strftime("%A"),'desc1':desc[0],'desc2':desc[1],'link':link})
    else:
        return redirect('login_p2')

# function to the url - 'requests_p2'
# functionality - for displaying requests page of website (phase2)
#                 ( requests page contains the requests by Individuals to accept their profiles)
#                 ( if request accepted - profile stored in central platform, else not stored )
def requests(request):
    if request.user.is_authenticated:
        username = request.user.username
        obj = Institution.objects.get(username=username)
        if obj.institution_field == 'Engineering':
            if obj.institution_type == 'College':
                objs = EnggClg_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = EnggUni_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
        elif obj.institution_field == 'Medical':
            if obj.institution_type == 'College':
                objs = MediClg_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = MediUni_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
        elif obj.institution_field == 'Other':
            if obj.institution_type == 'College':
                objs = OthClg_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = OthUni_Alumni.objects.filter(accepted=False).filter(institution_name=obj.institution_name)

        objs_l = list(objs)
        if len(objs_l)>0 :
            obj = objs_l[0]
        else:
            obj = None
        if request.method == 'POST':
            recipients = []
            recipients.append(obj.person_email)
            subject = "reg-Profile request"
            status = request.POST['status']
            if status == "accept":
                obj.accepted = True
                obj.save()
                message = "Your profile is accepted by us. Thank you!! - regards "+obj.institution_name
            elif status == "reject":
                obj.delete()
                message = "Your profile is rejected by us. - regards "+obj.institution_name
            o = Institution.objects.get(username=username)
            from_mail = o.alt_email
            message1 = "You got this mail via ATS website, sent by "+from_mail+"\n\n name-"+o.institution_name+"\n\nmessage-\n"
            print(from_mail)
            print(recipients)
            print(subject)
            print(message)
            send_mail(subject,message1+message,from_mail,recipients,fail_silently=False)
            return redirect('alumni_p2')
        if obj is None :
            return redirect('alumni_p2')
        email = obj.person_email
        objr = User.objects.get(email = email)
        name = objr.first_name + " " + objr.last_name
        if Profile_personal.objects.filter(username = objr.username).exists():
            obj1 = Profile_personal.objects.get(username = objr.username)
            b1 = True
        else :
            obj1 = None
            b1 = False

        if Profile_highEdu.objects.filter(username = objr.username).exists():
            obj2 = Profile_secEdu.objects.get(username = objr.username)
            obj3 = Profile_hsecEdu.objects.get(username = objr.username)
            obj4 = Profile_highEdu.objects.get(username = objr.username)
            b2 = True
        else :
            obj2 = None
            obj3 = None
            obj4 = None
            b2 = False
    
        if Profile_pro.objects.filter(username = objr.username).exists():
            obj5 = Profile_pro.objects.get(username = objr.username)
            b3 = True
        else :
            obj5 = None
            year = 0
            b3 = False
        return render(request,'phase2/requests.html',{'name':name,'obj':obj,'obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4,'obj5':obj5,'b1':b1,'b2':b2,'b3':b3})
    else:
        return redirect('login_p2')

# function to the url - 'gender_p2'
# functionality - for displaying Alumni(filtered by gender) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def gender(request):
    if request.user.is_authenticated:
        male = "male"
        female = "female"
        other = "other"
        if request.method == 'POST':
            gender = request.POST['gender']
            username = request.user.username
            obj = Institution.objects.get(username=username)
            if obj.institution_field == 'Engineering':
                if obj.institution_type == 'College':
                    objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(person_gender=gender)
            elif obj.institution_field == 'Medical':
                if obj.institution_type == 'College':
                    objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(person_gender=gender)
            elif obj.institution_field == 'Other':
                if obj.institution_type == 'College':
                    objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(person_gender=gender)

            print(objs)
            objs_l = list(objs)      
            print(objs_l)  
            return render(request,'phase2/gender.html',{'b':'out','objs':objs_l,'count':len(objs_l),'gender':gender})
        return render(request,'phase2/gender.html',{'b':'in','gender':''})
    else:
        return redirect('login_p2')

# function to the url - 'branch_p2'
# functionality - for displaying Alumni(filtered by branch) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def branch(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            branch = request.POST['branch']
            username = request.user.username
            obj = Institution.objects.get(username=username)
            if obj.institution_field == 'Engineering':
                if obj.institution_type == 'College':
                    objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch)
                elif obj.institution_type == 'University':
                    objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch)
            elif obj.institution_field == 'Medical':
                if obj.institution_type == 'College':
                    objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch)
                elif obj.institution_type == 'University':
                    objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch)
            elif obj.institution_field == 'Other':
                if obj.institution_type == 'College':
                    objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch)
                elif obj.institution_type == 'University':
                    objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch)

            print(objs)
            objs_l = list(objs)      
            print(objs_l)  
            return render(request,'phase2/branch.html',{'b':'out','objs':objs_l,'count':len(objs_l),'branch':branch})
        return render(request,'phase2/branch.html',{'b':'in','branch':''})
    else:
        return redirect('login_p2')

# function to the url - 'year_p2'
# functionality - for displaying Alumni(filtered by year of passing) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def year(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            year = request.POST['year']
            username = request.user.username
            obj = Institution.objects.get(username=username)
            if obj.institution_field == 'Engineering':
                if obj.institution_type == 'College':
                    objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year)
            elif obj.institution_field == 'Medical':
                if obj.institution_type == 'College':
                    objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year)
            elif obj.institution_field == 'Other':
                if obj.institution_type == 'College':
                    objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year)

            print(objs)
            objs_l = list(objs)      
            print(objs_l)  
            return render(request,'phase2/year.html',{'b':'out','objs':objs_l,'count':len(objs_l),'year':year})
        return render(request,'phase2/year.html',{'b':'in','year':''})
    else:
        return redirect('login_p2')

# function to the url - 'gender_branch_p2'
# functionality - for displaying Alumni(filtered by gender,branch) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def gender_branch(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            branch = request.POST['branch']
            gender = request.POST['gender']
            username = request.user.username
            obj = Institution.objects.get(username=username)
            if obj.institution_field == 'Engineering':
                if obj.institution_type == 'College':
                    objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender)
            elif obj.institution_field == 'Medical':
                if obj.institution_type == 'College':
                    objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender)
            elif obj.institution_field == 'Other':
                if obj.institution_type == 'College':
                    objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender)

            print(objs)
            objs_l = list(objs)      
            print(objs_l)  
            return render(request,'phase2/gender_branch.html',{'b':'out','objs':objs_l,'count':len(objs_l),'gender':gender,'branch':branch})
        return render(request,'phase2/gender_branch.html',{'b':'in','gender':'','branch':''})
    else:
        return redirect('login_p2')

# function to the url - 'gender_year_p2'
# functionality - for displaying Alumni(filtered by gender,year of passing) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def gender_year(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            gender = request.POST['gender']
            year = request.POST['year']
            username = request.user.username
            obj = Institution.objects.get(username=username)
            if obj.institution_field == 'Engineering':
                if obj.institution_type == 'College':
                    objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year).filter(person_gender=gender)
            elif obj.institution_field == 'Medical':
                if obj.institution_type == 'College':
                    objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year).filter(person_gender=gender)
            elif obj.institution_field == 'Other':
                if obj.institution_type == 'College':
                    objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year).filter(person_gender=gender)
                elif obj.institution_type == 'University':
                    objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_year_pass=year).filter(person_gender=gender)

            print(objs)
            objs_l = list(objs)      
            print(objs_l)  
            return render(request,'phase2/gender_year.html',{'b':'out','objs':objs_l,'count':len(objs_l),'gender':gender,'year':year})
        return render(request,'phase2/gender_year.html',{'b':'in','gender':'','year':''})
    else:
        return redirect('login_p2')

# function to the url - 'branch_year_p2'
# functionality - for displaying Alumni(filtered by branch,year of passing) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def branch_year(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            branch = request.POST['branch']
            year = request.POST['year']
            username = request.user.username
            obj = Institution.objects.get(username=username)
            if obj.institution_field == 'Engineering':
                if obj.institution_type == 'College':
                    objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(institution_year_pass=year)
            elif obj.institution_field == 'Medical':
                if obj.institution_type == 'College':
                    objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(institution_year_pass=year)
            elif obj.institution_field == 'Other':
                if obj.institution_type == 'College':
                    objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(institution_year_pass=year)

            print(objs)
            objs_l = list(objs)      
            print(objs_l)  
            return render(request,'phase2/branch_year.html',{'b':'out','objs':objs_l,'count':len(objs_l),'branch':branch,'year':year})
        return render(request,'phase2/branch_year.html',{'b':'in','branch':'','year':''})
    else:
        return redirect('login_p2')

# function to the url - 'branch_gender_year_p2'
# functionality - for displaying Alumni(filtered by branch,gender,year of passing) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def branch_gender_year(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            branch = request.POST['branch']
            gender = request.POST['gender']
            year = request.POST['year']
            username = request.user.username
            obj = Institution.objects.get(username=username)
            if obj.institution_field == 'Engineering':
                if obj.institution_type == 'College':
                    objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender).filter(institution_year_pass=year)
            elif obj.institution_field == 'Medical':
                if obj.institution_type == 'College':
                    objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender).filter(institution_year_pass=year)
            elif obj.institution_field == 'Other':
                if obj.institution_type == 'College':
                    objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender).filter(institution_year_pass=year)
                elif obj.institution_type == 'University':
                    objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name).filter(institution_branch=branch).filter(person_gender=gender).filter(institution_year_pass=year)

            print(objs)
            objs_l = list(objs)      
            print(objs_l)  
            return render(request,'phase2/branch_gender_year.html',{'b':'out','objs':objs_l,'count':len(objs_l),'branch':branch,'gender':gender,'year':year})
        return render(request,'phase2/branch_gender_year.html',{'b':'in','branch':'','gender':'','year':''})
    else:
        return redirect('login_p2')

# function to the url - 'all_list_p2'
# functionality - for displaying Alumni(whole) list page of website (phase2)
#                 ( Alumni list is fetched from database )
def all_list(request):
    if request.user.is_authenticated:
        username = request.user.username
        obj = Institution.objects.get(username=username)
        if obj.institution_field == 'Engineering':
            if obj.institution_type == 'College':
                objs = EnggClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = EnggUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name)
        elif obj.institution_field == 'Medical':
            if obj.institution_type == 'College':
                objs = MediClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = MediUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name)
        elif obj.institution_field == 'Other':
            if obj.institution_type == 'College':
                objs = OthClg_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name)
            elif obj.institution_type == 'University':
                objs = OthUni_Alumni.objects.filter(accepted=True).filter(institution_name=obj.institution_name)

        objs_l = list(objs)
        return render(request,'phase2/all_list.html',{'objs':objs_l,'count':len(objs_l)})
    else:
        return redirect('login_p2')
