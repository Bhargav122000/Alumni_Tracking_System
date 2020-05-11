# this file include functionality to display home page of website (phase2)

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from . import models
from .models import *
from datetime import date
import datetime

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

# function to the url - 'home_p2'
# functionality - for displaying the home page of website (phase2)
def home(request):
    if request.user.is_authenticated:
        d = datetime.datetime.now()
        desc = month_history(d.month)
        link = "https://thisdayintechhistory.com/"+str(d.month)+"/"+str(d.day)+"/"
        month_dic = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        return render(request,'phase2/home.html',{'day':d.day,'month':month_dic[d.month],'year':d.year,'week':d.strftime("%A"),'desc1':desc[0],'desc2':desc[1],'link':link})
    else:
        return redirect('login_p2')

