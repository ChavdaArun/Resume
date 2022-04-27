from django.db import models
import datetime
import os

#Register page

class Register(models.Model):
    '''username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    confirmpassword = models.CharField(max_length=150)
    class Meta:
       db_table="register"   '''
    
    username = models.CharField(max_length=150)
    email= models.CharField(max_length=150)
    mobile = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    confirmpassword = models.CharField(max_length=150)
    class Meta:
           db_table="register1"




# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('img/', filename)

class Item(models.Model):
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    class Meta:
           db_table="demo_item1"


#insert personal details
class Personal(models.Model):
     R_id  = models. TextField(max_length=200)
     Fristname = models.TextField(max_length=191)
     secondname = models.TextField(max_length=191)
     lastname = models.TextField(max_length=191)
     title = models.TextField(max_length=191)
     email = models.TextField(max_length=191)
     mobile = models.TextField(max_length=15)
     dob = models.TextField(max_length=20)
     gender = models.TextField(max_length=15)
     phone = models.TextField(max_length=15)
     linkedln = models.TextField(max_length=500)
     language = models.TextField(max_length=50)
     R_id  = models.IntegerField(max_length=50)
   
     profilepicture = models.ImageField(upload_to=filepath, null=True, blank=True)
     about = models.TextField(max_length=1800)
     address  = models.TextField(max_length=750)
     class Meta:
           db_table="personal1"

# enter educationdetails
class Educationdetails(models.Model):
    r_id =  models. TextField(max_length=200)
    qulification = models.TextField(max_length=191)
    college = models.TextField(max_length=191)
    board = models.TextField(max_length=191)
    year = models.TextField(max_length=191)
    percentageclass = models.TextField(max_length=191)
    class Meta:
           db_table="education1"

# Experience Model

class Experience(models.Model) :
      r_id =  models. TextField(max_length=200)
      experience = models.CharField(max_length=100)
      companyname = models.CharField(max_length=100)
      startfrom = models.DateField()
      startto = models.DateField()
      programinglanguage = models.TextField(max_length=200)
      address = models. TextField(max_length=500)
      role = models.TextField(max_length=200)

      class Meta :
            db_table = 'experience1'

#  Skiles model     
class Skills(models.Model) :
      r_id =  models. TextField(max_length=200)
      title	= models. TextField(max_length=200)
      rating = models.CharField(max_length=100)
      class Meta :
            db_table = 'skiles1'

# Achivements model
class Achievements(models.Model) :
      r_id =  models. TextField(max_length=200)
      title = models.TextField(max_length=50)
      descrption = models. TextField(max_length=200)
      class Meta :
            db_table = 'achievements1'


 #contact
class Contact(models.Model):
      name =  models. TextField(max_length=200)
      email = models.TextField(max_length=50)
      subject = models. TextField(max_length=200)
      message	 = models. TextField(max_length=200)
     
      class Meta :
            db_table = 'contact'



