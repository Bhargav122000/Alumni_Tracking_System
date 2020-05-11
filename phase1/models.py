from django.db import models

# Create your models here.
class Profile_personal(models.Model):
    username = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=7)

class Profile_secEdu(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    year_join = models.SmallIntegerField()
    year_pass = models.SmallIntegerField()
    score = models.SmallIntegerField()
    state = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

class Profile_hsecEdu(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    year_join = models.SmallIntegerField()
    year_pass = models.SmallIntegerField()
    score = models.SmallIntegerField()
    state = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

class Profile_highEdu(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=50)
    ofType = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    year_join = models.SmallIntegerField()
    year_pass = models.SmallIntegerField()
    score = models.SmallIntegerField()
    state = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

class Profile_pro(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    year_join = models.SmallIntegerField()
    state = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    previous = models.TextField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150,default='-')
    title = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.ImageField(null=True,blank=True)
    venue = models.CharField(max_length=100)
    date_time = models.CharField(max_length=50)
    to_alumni = models.TextField()
    to_inst = models.TextField()

class forEmail(models.Model):
    file_name = models.FileField(null=True,blank=True)