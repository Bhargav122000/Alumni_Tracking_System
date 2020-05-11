# this file includes the functionality to display Events page of website (phase1)
# this file also includes the functionality to Create an Invitation for events,view available events

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

# function to the url - 'events_p1'
# functionality - for displaying the events page of website (phase1)
def events(request):
    if request.user.is_authenticated:
        d = datetime.datetime.now()
        desc = month_history(d.month)
        link = "https://thisdayintechhistory.com/"+str(d.month)+"/"+str(d.day)+"/"
        month_dic = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        return render(request,'phase1/events.html',{'day':d.day,'month':month_dic[d.month],'year':d.year,'week':d.strftime("%A"),'desc1':desc[0],'desc2':desc[1],'link':link})
    else :
        return redirect('login_p1')

# function to the url - 'event_generate_p1'
# functionality - for displaying Event Invitation generation page (phase1)
#                 ( the event invitation details stored in database)
def event_generate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            to_alumni = []
            to_inst = []
            name = request.user.first_name+" "+request.user.last_name
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
            return redirect('events_p1')
        alumni_list = []
        inst_list = []
        list_users = list(User.objects.all())
        my_name = request.user.first_name+" "+request.user.last_name
        for u in list_users:
            if u.username.find('@engg.clg')>0 or u.username.find('@engg.uni')>0 or u.username.find('@medi.clg')>0 or u.username.find('@medi.uni')>0 or u.username.find('@oth.clg')>0 or u.username.find('@oth.uni')>0 :
                obj = Institution.objects.get(username = u.username)
                name = obj.institution_name
                inst_list.append(name)
            else:
                if(len(u.first_name)>0 or len(u.last_name)>0):
                    name = u.first_name + " " + u.last_name
                    if my_name != name:
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
        return render(request,'phase1/event_generate.html',{'alumni_list':alumni_list,'inst_list':inst_list,'b1':b1,'b2':b2})
    else:
        return redirect('login_p1')

# function to the url - 'event_list_p1'
# functionality - for displaying Event Invitation list (available events) page (phase1)
#                 ( the event invitation details are fetched from database)
def event_list(request):
    if request.user.is_authenticated:
        obj_list = list(Event.objects.all())
        name_list = []
        events = []
        today = str(datetime.datetime.now())
        dt2 = datetime.datetime(int(today[0:4]),int(today[5:7]),int(today[8:10]))
        name = request.user.first_name+" "+request.user.last_name
        for obj in obj_list:
            print(obj.name)
            if obj.name != name:
                print(obj.to_alumni)
                print(obj.date_time)
                print(obj.attachment)
                name_list = eval(obj.to_alumni)
                dt1 = datetime.datetime(int(obj.date_time[0:4]),int(obj.date_time[5:7]),int(obj.date_time[8:10]))
                for n in name_list:
                    if name == n :
                        if dt1 > dt2 :
                            events.append(obj)
            
        print(events)
        return render(request,'phase1/event_list.html',{'events':events})
    else:
        return redirect('login_p1')

# function to the url - 'my_event_list_p1'
# functionality - for displaying Event Invitation list (event invitations by logged-in member) page (phase1)
#                 ( the event invitation details are fetched from database)
def my_event_list(request):
    if request.user.is_authenticated:
        obj_list = list(Event.objects.all())
        events = []
        name = request.user.first_name+" "+request.user.last_name
    
        if len(obj_list)>0:
            for obj in obj_list:
                if obj.name == name:
                    events.append(obj)
    
        return render(request,'phase1/my_event_list.html',{'events':events})
    else:
        return redirect('login_p1')