# this file includes functionalities for displaying Profile page of website (phase1)
# this file also includes functionalities for creating,viewing,updating,merging profile of alumni member (phase1)

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from . import models
from .models import *
from datetime import date
from phase2.models import *
from django.conf import settings
import datetime
import urllib.request
from os.path import realpath

# function used by below functions for getting the month history
def month_history(month):
    desc = []
    if month == 1:
        desc.append("Janus's month") 
        desc.append("Janus is the Roman god of gates and doorways, depicted with two faces looking in opposite directions. His festival month is January")
    elif month == 2:
        desc.append("month of Februa")
        desc.append("Februa is the Roman festival of purification, held on February fifteenth. It is possibly of Sabine origin.")
    elif month == 3:
        desc.append("Mars' month")
        desc.append("Mars is the Roman god of war. He is identified with the Greek god Ares.")
    elif month == 4:
        desc.append("Aphrodite's month")
        desc.append("Aphrodite is the Greek goddess of love and beauty. She is identified with the Roman goddess Venus.")
    elif month == 5:
        desc.append("Maia's month")
        desc.append("Maia (meaning 'the great one') is the Italic goddess of spring, the daughter of Faunus, and wife of Vulcan.")
    elif month == 6:
        desc.append("Juno's month")
        desc.append("Juno is the principle goddess of the Roman Pantheon. She is the goddess of marriage and the well-being of women. She is the wife and sister of Jupiter. She is identified with the Greek goddess Hera.")
    elif month == 7:
        desc.append("Julius Caesar's month")
        desc.append("Julius Caesar reformed the Roman calendar (hence the Julian calendar) in 46 BC. In the process, he renamed this month after himself.")
    elif month == 8:
        desc.append("Augustus Caesar's month")
        desc.append("Augustus Caesar clarified and completed the calendar reform of Julius Caesar. In the process, he also renamed this month after himself.")
    elif month == 9:
        desc.append("the seventh month")
        desc.append("")
    elif month == 10:
        desc.append("the eighth month")
        desc.append("")
    elif month == 11:
        desc.append("the nineth month")
        desc.append("")
    elif month == 12:
        desc.append("the tenth month")
        desc.append("")
    return desc

# function to the url - 'profile_p1'
# functionality - for displaying profile page of website (phase1)
def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        if Profile_personal.objects.filter(username=username).exists():
            b1 = True
        else:
            b1 = False

        if Profile_highEdu.objects.filter(username=username).exists():
            b2 = True
        else:
            b2 = False

        if Profile_pro.objects.filter(username=username).exists():
            b3 = True
        else:
            b3 = False

        if b1 and b2 and b3 :
            b_create = False
            b_merge = True
        else:
            b_create = True
            b_merge = False

        if b1 or b2 or b3 :
            b_view = True
            b_edit = True
        else:
            b_view = False
            b_edit = False
    
        d = datetime.datetime.now()
        desc = month_history(d.month)
        link = "https://thisdayintechhistory.com/"+str(d.month)+"/"+str(d.day)+"/"
        month_dic = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        return render(request,'phase1/profile.html',{'day':d.day,'month':month_dic[d.month],'year':d.year,'week':d.strftime("%A"),'desc1':desc[0],'desc2':desc[1],'link':link,'b_create':b_create,'b_view':b_view,'b_edit':b_edit,'b_merge':b_merge})
    else :
        return redirect('login_p1')

# function to the url - 'create_profile_p1'
# functionality - for displaying Profile creation page of website (phase1)
def create_profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        if Profile_personal.objects.filter(username = username).exists():
            b1 = True
        else : 
            b1 = False

        if Profile_highEdu.objects.filter(username = username).exists():
            b2 = True
        else :
            b2 = False

        if Profile_pro.objects.filter(username = username).exists():
            b3 = True
        else:
            b3 = False

        if b1 and b2 and b3:
            return redirect('profile_p1')
        else:
            return render(request,'phase1/profile_create.html',{'b1':b1,'b2':b2,'b3':b3})
    else:
        return redirect('login_p1')

# function to the url - 'create_personal_p1'
# functionality - for displaying Page for creating personal profile,
#                 and also creating the Personal profile of logged-in alumni member
#                 and storing it in database (phase1)
def create_personal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.user.username
            dob = request.POST['dob']
            gender = request.POST['gender']
            mother_name = request.POST['mother_name']
            father_name = request.POST['father_name']
            phone = request.POST['phone']
            state = request.POST['state']
            place = request.POST['place']
            address = request.POST['address']
            pincode = request.POST['pincode']

            obj1 = Profile_personal(username=username,dob=dob,gender=gender,mother_name=mother_name,father_name=father_name,phone=phone,state=state,place=place,address=address,pincode=pincode)
            obj1.save()
            return redirect('create_profile_p1')

        states = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        return render(request,'phase1/personal.html',{'states':states})
    else:
        return redirect('login_p1')

# function to the url - 'create_educational_p1'
# functionality - for displaying Page for creating educational profile,
#                 and also creating the Educational profile of logged-in alumni member
#                 and storing it in database (phase1)
def create_educational(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.user.username

            school_name = request.POST['school_name']
            school_join = request.POST['school_join']
            school_pass = request.POST['school_pass']
            school_score = request.POST['school_score']
            school_state = request.POST['school_state']
            school_place = request.POST['school_place']
        
            obj = Profile_secEdu(username=username,name=school_name,year_join=school_join,year_pass=school_pass,score=school_score,state=school_state,place=school_place)
            obj.save()
        
            college_name = request.POST['college_name']
            college_branch = request.POST['college_branch']
            college_join = request.POST['college_join']
            college_pass = request.POST['college_pass']
            college_score = request.POST['college_score']
            college_state = request.POST['college_state']
            college_place = request.POST['college_place']

            obj = Profile_hsecEdu(username=username,name=college_name,branch=college_branch,year_join=college_join,year_pass=college_pass,score=college_score,state=college_state,place=college_place)
            obj.save()
        
            inst_name = request.POST['inst_name']
            inst_field = request.POST['inst_field']
            inst_type = request.POST['inst_type']
            if inst_field == 'Engineering':
                inst_branch = request.POST['inst_engg_branch']
            elif inst_field == 'Medical':
                inst_branch = request.POST['inst_medi_branch']
            else :
                inst_branch = request.POST['inst_other_branch']
            inst_join = request.POST['inst_join']
            inst_pass = request.POST['inst_pass']
            inst_score = request.POST['inst_score']
            inst_state = request.POST['inst_state']
            inst_place = request.POST['inst_place']
        
            obj = Profile_highEdu(username=username,name=inst_name,branch=inst_branch,year_join=inst_join,year_pass=inst_pass,score=inst_score,state=inst_state,place=inst_place,field=inst_field,ofType=inst_type)
            obj.save()
        
            return redirect('create_profile_p1')

        medi_branches = ['MBBS','BDS','BHMS','BAMS','DHMS','BUMS','B.V.Sc & AH','B.Pharm','D.Pharma','BOT','BMLT','BPT','B.Sc.Nursing','BNYS','Other']
        engg_branches = ['Civil','Mechanical','Electrical','Electrical & Electronics','Electronics & Communication','Computer Science','Biotechnology','Electronics & Instrumentation','Information Technology','Automobile','Aeronautical','Architectural','Agricultural','Petroleum','Food Technology','Textile','Chemical','Biochemical','Aerospace','Industrial','Manufacturing','Material','Mechatronics','Genetic','Ocean & Marine','Mining']
        states = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        return render(request,'phase1/educational.html',{'states':states,'medi_branches':medi_branches,'engg_branches':engg_branches})
    else:
        return redirect('login_p1')

# function to the url - 'create_professional_p1'
# functionality - for displaying Page for creating professional profile,
#                 and also creating the Professional profile of logged-in alumni member
#                 and storing it in database (phase1)
def create_professional(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.user.username
            pro_name = request.POST['pro_name']
            pro_role = request.POST['pro_role']
            pro_join = request.POST['pro_join']
            pro_state = request.POST['pro_state']
            pro_place = request.POST['pro_place']
            pro_previous = request.POST['pro_previous']
        
            obj = Profile_pro(username=username,name=pro_name,role=pro_role,year_join=pro_join,state=pro_state,place=pro_place,previous=pro_previous)
            obj.save()
        
            return redirect('create_profile_p1')

        states = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        return render(request,'phase1/professional.html',{'states':states})
    else:
        return redirect('login_p1')
        
# function to the url - 'view_profile_p1'
# functionality - for displaying Profile View page of website (phase1)
#                 (profile of logged-in alumni member is fetched from database)
def view_profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        if Profile_personal.objects.filter(username = username).exists():
            obj1 = Profile_personal.objects.get(username = username)
            b1 = True
        else :
            obj1 = None
            b1 = False

        if Profile_highEdu.objects.filter(username = username).exists():
            obj2 = Profile_secEdu.objects.get(username = username)
            obj3 = Profile_hsecEdu.objects.get(username = username)
            obj4 = Profile_highEdu.objects.get(username = username)
            b2 = True
        else :
            obj2 = None
            obj3 = None
            obj4 = None
            b2 = False
    
        if Profile_pro.objects.filter(username = username).exists():
            obj5 = Profile_pro.objects.get(username = username)
            b3 = True
        else :
            obj5 = None
            year = 0
            b3 = False
        if b1==False and b2==False and b3==False:
            return redirect('profile_p1')
        b = [b1,b2,b3]
        return render(request,'phase1/profile_view.html',{'obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4,'obj5':obj5,'b1':b1,'b2':b2,'b3':b3})
    else:
        return redirect('login_p1')

# function to the url - 'edit_profile_p1'
# functionality - for displaying Profile Edit/Update page of website (phase1)
#                 (logged-in alumni member is given facility to edit/update Profile)
def edit_profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        if Profile_personal.objects.filter(username = username).exists():
            b1 = True
        else : 
            b1 = False

        if Profile_highEdu.objects.filter(username = username).exists():
            b2 = True
        else :
            b2 = False

        if Profile_pro.objects.filter(username = username).exists():
            b3 = True
        else:
            b3 = False
        if b1==False and b2==False and b3==False :
            return redirect('profile_p1')
        else :
            return render(request,'phase1/profile_edit.html',{'b1':b1,'b2':b2,'b3':b3})
    else:
        return redirect('login_p1')

# function to the url - 'edit_personal_p1'
# functionality - for displaying Page for editing/updating personal profile,
#                 and also editing/updating the Personal profile of logged-in alumni member
#                 and storing it in database (phase1)
def edit_personal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dob = request.POST['dob']
            gender = request.POST['gender']
            mother_name = request.POST['mother_name']
            father_name = request.POST['father_name']
            phone = request.POST['phone']
            state = request.POST['state']
            place = request.POST['place']
            address = request.POST['address']
            pincode = request.POST['pincode']
        
            obj = Profile_personal.objects.get(username=request.user.username)
            obj.dob = dob
            obj.gender = gender
            obj.mother_name = mother_name
            obj.father_name = father_name
            obj.phone = phone
            obj.state = state
            obj.place = place
            obj.address = address
            obj.pincode = pincode
            obj.save()
            return redirect('edit_profile_p1')

        obj = Profile_personal.objects.get(username=request.user.username)
        states = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        return render(request,'phase1/personal_edit.html',{'obj':obj,'states':states})
    else:
        return redirect('login_p1')

# function to the url - 'edit_educational_p1'
# functionality - for displaying Page for editing/updating educational profile,
#                 and also editing/updating the Educational profile of logged-in alumni member
#                 and storing it in database (phase1)
def edit_educational(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            school_name = request.POST['school_name']
            school_join = request.POST['school_join']
            school_pass = request.POST['school_pass']
            school_score = request.POST['school_score']
            school_state = request.POST['school_state']
            school_place = request.POST['school_place']
            obj = Profile_secEdu.objects.get(username=request.user.username)
            obj.name = school_name
            obj.year_join = school_join
            obj.year_pass = school_pass
            obj.score = school_score
            obj.state = school_state
            obj.place = school_place
            obj.save()

            college_name = request.POST['college_name']
            college_branch = request.POST['college_branch']
            college_join = request.POST['college_join']
            college_pass = request.POST['college_pass']
            college_score = request.POST['college_score']
            college_state = request.POST['college_state']
            college_place = request.POST['college_place']
            obj = Profile_hsecEdu.objects.get(username=request.user.username)
            obj.name = college_name
            obj.branch = college_branch
            obj.year_join = college_join
            obj.year_pass = college_pass
            obj.score = college_score
            obj.state = college_state
            obj.place = college_place
            obj.save()

            inst_name = request.POST['inst_name']
            inst_field = request.POST['inst_field']
            inst_type = request.POST['inst_type']
            if inst_field == 'Engineering':
                inst_branch = request.POST['inst_engg_branch']
            elif inst_field == 'Medical':
                inst_branch = request.POST['inst_medi_branch']
            else :
                inst_branch = request.POST['inst_other_branch']
            inst_join = request.POST['inst_join']
            inst_pass = request.POST['inst_pass']
            inst_score = request.POST['inst_score']
            inst_state = request.POST['inst_state']
            inst_place = request.POST['inst_place']
            obj = Profile_highEdu.objects.get(username=request.user.username)
            obj.name = inst_name
            obj.field = inst_field
            obj.ofType = inst_type
            obj.branch = inst_branch
            obj.year_join = inst_join
            obj.year_pass = inst_pass
            obj.score = inst_score
            obj.state = inst_state
            obj.place = inst_place
            obj.save()
            return redirect('edit_profile_p1')
        obj1 = Profile_secEdu.objects.get(username=request.user.username)
        obj2 = Profile_hsecEdu.objects.get(username=request.user.username)
        obj3 = Profile_highEdu.objects.get(username=request.user.username)
        medi_branches = ['MBBS','BDS','BHMS','BAMS','DHMS','BUMS','B.V.Sc & AH','B.Pharm','D.Pharma','BOT','BMLT','BPT','B.Sc.Nursing','BNYS','Other']
        engg_branches = ['Civil','Mechanical','Electrical','Electrical & Electronics','Electronics & Communication','Computer Science','Biotechnology','Electronics & Instrumentation','Information Technology','Automobile','Aeronautical','Architectural','Agricultural','Petroleum','Food Technology','Textile','Chemical','Biochemical','Aerospace','Industrial','Manufacturing','Material','Mechatronics','Genetic','Ocean & Marine','Mining']
        states = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        return render(request,'phase1/educational_edit.html',{'obj1':obj1,'obj2':obj2,'obj3':obj3,'states':states,'medi_branches':medi_branches,'engg_branches':engg_branches})
    else:
        return redirect('login_p1')

# function to the url - 'edit_professional_p1'
# functionality - for displaying Page for editing/updating of professional profile,
#                 and also editing/updating the Professional profile of logged-in alumni member
#                 and storing it in database (phase1)
def edit_professional(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pro_name = request.POST['pro_name']
            pro_role = request.POST['pro_role']
            pro_join = request.POST['pro_join']
            pro_state = request.POST['pro_state']
            pro_place = request.POST['pro_place']
            pro_previous = request.POST['pro_previous']
        
            obj = Profile_pro.objects.get(username=request.user.username)
            obj.name = pro_name
            obj.role = pro_role
            obj.year_join = pro_join
            obj.state = pro_state
            obj.place = pro_place
            obj.previous = pro_previous
            obj.save()
            return redirect('edit_profile_p1')

        obj = Profile_pro.objects.get(username=request.user.username)
        states = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
        return render(request,'phase1/professional_edit.html',{'obj':obj,'states':states})
    else:
        return redirect('login_p1')

# function to the url - 'merge_p1'
# functionality - for sending a request of accepting profile and merge it into central platform (phase1)
#                 (profile of logged-in alumni member is sent to respective instituion)
def merge(request):
    if request.user.is_authenticated:
        username = request.user.username
        name = request.user.first_name + " " + request.user.last_name
        email = request.user.email

        if Profile_personal.objects.filter(username=username).exists():
            if Profile_highEdu.objects.filter(username=username).exists():
                if Profile_pro.objects.filter(username=username).exists():
                    obj1 = Profile_personal.objects.get(username=username)
                    obj2 = Profile_highEdu.objects.get(username=username)
                    obj3 = Profile_pro.objects.get(username=username)

                    if obj2.field == 'Engineering':
                        if obj2.ofType == 'College':
                            if EnggClg_Alumni.objects.filter(person_name=name).filter(institution_name=obj2.name).filter(institution_branch=obj2.branch).filter(institution_year_pass=obj2.year_pass).filter(company_name=obj3.name).exists():
                                obj = EnggClg_Alumni.objects.get(person_email = email)
                            else :
                                obj = EnggClg_Alumni()
                        elif obj2.ofType == 'University':
                            if EnggUni_Alumni.objects.filter(person_name=name).filter(institution_name=obj2.name).filter(institution_branch=obj2.branch).filter(institution_year_pass=obj2.year_pass).filter(company_name=obj3.name).exists():
                                obj = EnggUni_Alumni.objects.get(person_email = email)
                            else :
                                obj = EnggUni_Alumni()
                    elif obj2.field == 'Medical':
                        if obj2.ofType == 'College':
                            if MediClg_Alumni.objects.filter(person_name=name).filter(institution_name=obj2.name).filter(institution_branch=obj2.branch).filter(institution_year_pass=obj2.year_pass).filter(company_name=obj3.name).exists():
                                obj = MediClg_Alumni.objects.get(person_email = email)
                            else :
                                obj = MediClg_Alumni()
                        elif obj2.ofType == 'University':
                            if MediUni_Alumni.objects.filter(person_name=name).filter(institution_name=obj2.name).filter(institution_branch=obj2.branch).filter(institution_year_pass=obj2.year_pass).filter(company_name=obj3.name).exists():
                                obj = MediUni_Alumni.objects.get(person_email = email)
                            else :
                                obj = MediUni_Alumni()
                    elif obj2.field == 'Other':
                        if obj2.ofType == 'College':
                            if OthClg_Alumni.objects.filter(person_name=name).filter(institution_name=obj2.name).filter(institution_branch=obj2.branch).filter(institution_year_pass=obj2.year_pass).filter(company_name=obj3.name).exists():
                                obj = OthClg_Alumni.objects.get(person_email = email)
                            else :
                                obj = OthClg_Alumni()
                        elif obj2.ofType == 'University':
                            if OthUni_Alumni.objects.filter(person_name=name).filter(institution_name=obj2.name).filter(institution_branch=obj2.branch).filter(institution_year_pass=obj2.year_pass).filter(company_name=obj3.name).exists():
                                obj = OthUni_Alumni.objects.get(person_email = email)
                            else :
                                obj = OthUni_Alumni()
                 
                    obj.person_name = name
                    obj.person_email = email
                    obj.person_gender = obj1.gender
                    obj.person_phone = obj1.phone
                    obj.institution_name = obj2.name
                    obj.institution_branch = obj2.branch
                    obj.institution_year_pass = obj2.year_pass
                    obj.institution_state = obj2.state
                    obj.institution_place = obj2.place
                    obj.company_name = obj3.name
                    obj.company_role = obj3.role
                    obj.company_year_join = obj3.year_join
                    obj.company_state = obj3.state
                    obj.company_place = obj3.place
                    obj.company_previous = obj3.previous
                    obj.save()

                    print('merge request is sent successfully')
                    return redirect('profile_p1')
                else :
                    print('Do not have a professional profile')
                    return redirect('profile_p1')
            else :
                print('Do not have educational profile')
                return redirect('profile_p1')
        else :
            print('Do not have a personal profile')
            return redirect('profile_p1')
    else:
        return redirect('login_p1')


