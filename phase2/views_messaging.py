# this file includes functionality to display Messaging page of website (phase2)
# this file also includes functionality for sending messages from one to other by Mails

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from . import models
from .models import *
from datetime import date
from django.core.mail import send_mail,EmailMessage
from .views_home import month_history
from phase1.models import *
import datetime

# function to the url - 'messaging_p2'
# functionality - for displaying Messaging page of website (phase2)
#                 for sending message with an attachment by logged-in Institution by Mails to others.
def messaging(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Institution.objects.get(username=request.user.username)
            recipients = []
            from_mail = request.POST['from_mail']
            subject = request.POST['subject']
            message3 = request.POST['message']
            attachment = request.FILES['attachment']
            obj1 = forEmail(file_name=attachment)
            obj1.save()
            count = request.POST['count']
            count = int(count)
            message1 = "You got this mail via ATS website, sent by:\n "
            message2 = from_mail+"\n"+"name:"+obj.institution_name+"\n\nmessage -\n"
            print(count)
            print(type(count))
            if count == 0:
                return redirect('messaging_p2')
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
                p1 = "static/files/"+str(obj1.file_name)
                msg.attach_file(p1)
                msg.send()
                #send_mail(subject,message1+message2+message3,from_mail,recipients,fail_silently=False)
            else:
                print('no recipients selected')
            
            obj1.delete()
            return redirect('messaging_p2')
        else:
            gmail1 = request.user.email
            obj = Institution.objects.get(username=request.user.username)
            gmail2 = obj.alt_email
            d = datetime.datetime.now()
            desc = month_history(d.month)
            link = "https://thisdayintechhistory.com/"+str(d.month)+"/"+str(d.day)+"/"
            month_dic = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
            return render(request,'phase2/messaging.html',{'gmail1':gmail1,'gmail2':gmail2,'day':d.day,'month':month_dic[d.month],'year':d.year,'week':d.strftime("%A"),'desc1':desc[0],'desc2':desc[1],'link':link})
    else:
        return redirect('login_p2')
