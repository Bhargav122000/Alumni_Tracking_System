# this file includes functionality to display Messaging page of website (phase1)
# this file also includes functionality for sending messages from one to other by Mails

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from . import models
from .models import *
from datetime import date
from django.core.mail import send_mail,EmailMessage
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

# function to the url - 'messaging_p1'
# functionality - for displaying Messaging page of website (phase1)
#                 for sending message with an attachment by logged-in alumni member by Mails to others.
def messaging(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            recipients = []
            subject = request.POST['subject']
            message3 = request.POST['message']
            attachment = request.FILES['attachment']
            obj = forEmail(file_name=attachment)
            obj.save()
            from_mail = request.user.email
            count = request.POST['count']
            count = int(count)
            message1 = "You got this mail via ATS website, sent by:\n "
            message2 = from_mail+"\n"+"name:"+request.user.first_name+" "+request.user.last_name+"\n\nmessage -\n"
            print(count)
            print(type(count))
            if count == 0:
                return redirect('messaging_p1')
            for i in range(count):
                r = request.POST['to'+str(i+1)]
                if len(r)>0 :
                    recipients.append(request.POST['to'+str(i+1)])
            
            print(subject)
            print(message3)
            print(from_mail)
            print(recipients)
            print(type(recipients))
            
            if len(recipients)>0:
                msg = EmailMessage(subject, message1+message2+message3, from_mail, recipients)
                #msg.content_subtype = "html"  
                p1 = "static/files/"+str(obj.file_name)
                msg.attach_file(p1)
                msg.send()
                #send_mail(subject,message1+message,from_mail,recipients,fail_silently=False)
            else:
                print('no recipients selected')
            obj.delete()
            return redirect('messaging_p1')
        else :
            d = datetime.datetime.now()
            desc = month_history(d.month)
            link = "https://thisdayintechhistory.com/"+str(d.month)+"/"+str(d.day)+"/"
            month_dic = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
            return render(request,'phase1/messaging.html',{'day':d.day,'month':month_dic[d.month],'year':d.year,'week':d.strftime("%A"),'desc1':desc[0],'desc2':desc[1],'link':link})
    else :
        return redirect('login_p1')
