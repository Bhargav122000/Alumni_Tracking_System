# this file includes the functionality to display Events page of website (phase2)
# this file also includes the functionality to Create an Invitation for events,view available events

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from . import models
from .models import *
from datetime import date
from .views_home import month_history
from phase1.models import *
import datetime

# function to the url - 'events_p2'
# functionality - for displaying the events page of website (phase2)
def events(request):
    if request.user.is_authenticated:
        d = datetime.datetime.now()
        desc = month_history(d.month)
        link = "https://thisdayintechhistory.com/"+str(d.month)+"/"+str(d.day)+"/"
        month_dic = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        return render(request,'phase2/events.html',{'day':d.day,'month':month_dic[d.month],'year':d.year,'week':d.strftime("%A"),'desc1':desc[0],'desc2':desc[1],'link':link})
    else:
        return redirect('login_p2')

# function to the url - 'event_generate_p2'
# functionality - for displaying Event Invitation generation page (phase2)
#                 ( the event invitation details stored in database)
def event_generate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            to_alumni = []
            to_inst = []
            name = Institution.objects.get(username=request.user.username).institution_name
            email = request.user.email
            title = request.POST['title']
            description = request.POST['description']
            attachment = request.FILES['attachment']
            print(attachment)
            print(type(attachment))
            venue = request.POST['venue']
            date_time = request.POST['date_time']
            to_alumni = request.POST.getlist('to_alumni[]')
            to_inst = request.POST.getlist('to_inst[]')

            obj = Event(name=name,title=title,description=description,attachment=attachment,venue=venue,date_time=date_time,to_alumni=str(to_alumni),to_inst=str(to_inst),email=email)
            obj.save()
        
            #print(title)
            #print(type(title))
            #print(description)
            #print(type(description))
            #print(attachment)
            #print(type(attachment))
            #print(venue)
            #print(type(venue))
            #print(date_time)
            #print(type(date_time))
            #print(to_alumni)
            #print(type(to_alumni))
            #print(to_inst)
            #print(type(to_inst))

            #print(str(to_alumni))
            #print(str(to_inst))
            return redirect('events_p2')
        alumni_list = []
        inst_list = []
        list_users = list(User.objects.all())
        my_name = Institution.objects.get(username=request.user.username).institution_name
        for u in list_users:
            if u.username.find('@engg.clg')>0 or u.username.find('@engg.uni')>0 or u.username.find('@medi.clg')>0 or u.username.find('@medi.uni')>0 or u.username.find('@oth.clg')>0 or u.username.find('@oth.uni')>0 :
                obj = Institution.objects.get(username = u.username)
                name = obj.institution_name
                if my_name != name:
                    inst_list.append(name)
            else:
                if(len(u.first_name)>0 or len(u.last_name)>0):
                    name = u.first_name + " " + u.last_name
                    alumni_list.append(name)
        print(list_users)
        print(alumni_list)
        print(inst_list)
        if len(alumni_list)>0:
            b1 = True
        else:
            b1 = False

        if len(inst_list)>0:
            b2 = True
        else:
            b2 = False
        return render(request,'phase2/event_generate.html',{'alumni_list':alumni_list,'inst_list':inst_list,'b1':b1,'b2':b2})
    else:
        return redirect('login_p2')

# function to the url - 'event_list_p2'
# functionality - for displaying Event Invitation list (available events) page (phase2)
#                 ( the event invitation details are fetched from database)
def event_list(request):
    if request.user.is_authenticated:
        obj_list = list(Event.objects.all())
        name_list = []
        events = []
        today = str(datetime.datetime.now())
        dt2 = datetime.datetime(int(today[0:4]),int(today[5:7]),int(today[8:10]))
        name = Institution.objects.get(username=request.user.username).institution_name
        print(name)
        for obj in obj_list:
            print(obj.name)
            if obj.name != name:
                print(obj.to_alumni)
                print(obj.date_time)
                print(obj.attachment)
                name_list = eval(obj.to_inst)
                dt1 = datetime.datetime(int(obj.date_time[0:4]),int(obj.date_time[5:7]),int(obj.date_time[8:10]))
                for n in name_list:
                    if name == n :
                        if dt1 > dt2 :
                            events.append(obj)
            
        print(events)
        return render(request,'phase2/event_list.html',{'events':events})
    else:
        return redirect('login_p2')

# function to the url - 'my_event_list_p2'
# functionality - for displaying Event Invitation list (event invitations by logged-in institution) page (phase2)
#                 ( the event invitation details are fetched from database)
def my_event_list(request):
    if request.user.is_authenticated:
        obj_list = list(Event.objects.all())
        events = []
        name = Institution.objects.get(username=request.user.username).institution_name
    
        if len(obj_list)>0:
            for obj in obj_list:
                if obj.name == name:
                    events.append(obj)
    
        return render(request,'phase2/my_event_list.html',{'events':events})
    else:
        return redirect('login_p2')