from typing import ContextManager
from onlinecv.settings import RAZOR_KEY_ID, RAZOR_KEY_SECRET
import razorpay
from django.shortcuts import render
from django.db import connection
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect,HttpResponse

from django.core.mail import send_mail  

from django.conf import settings
from  demo.models import Item
from  demo.models import Educationdetails
from  demo.models import Personal
from  demo.models import Register
from  demo.models import Achievements
from  demo.models import Skills
from  demo.models import Experience
from  demo.models import Contact


from django.contrib import messages



# Create your views here.

#indexpage


def index(request):
    context = Item.objects.all()
    if request.method == "POST":
        cont = Contact()
        cont.name = request.POST.get('name')
        cont.email = request.POST.get('email')
        cont.subject = request.POST.get('subject')
        cont.message = request.POST.get('message')
        cont.save()

    
    return render(request,'index.html',{'objec':context})
    
#add dyanmic Resume

def AddResume(request):
      if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return render(request,'AddResume.html')
      else:
                  return render(request,'AddResume.html')   


#resuem
def Resume(request):
     return render(request,'Resume.html')




#Registerpage
def register(request):
    
    if request.method=='POST':
        # Password verify
        if request.POST.get('password') == request.POST.get('confirmpassword'):

            # Email Verification
            
            val = Register.objects.filter(email=request.POST.get('email')).count()
            data = Register.objects.all()

            if val == 1:
                messages.warning(request, 'Email is already exist ...!')
                return render(request,'register.html') 

            else:
                # Database code
                if request.POST.get('username') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('password')  and request.POST.get('confirmpassword') :
                

                    saverecord=Register()
                    saverecord.username=request.POST.get('username')
                    saverecord.email=request.POST.get('email')
                    saverecord.mobile=request.POST.get('mobile')
                    saverecord.password=request.POST.get('password')
                    saverecord.confirmpassword=request.POST.get('confirmpassword')
                    
                    
                    saverecord.save()

                    return redirect('login')
                
                else:
                    messages.success(request, 'One Field is Empty ...!')
                    return render(request,'register.html')

        else:
            messages.success(request, 'Password Not Match ...!')
            return render(request,'register.html')
    else:
        return render(request,'register.html')


#Login
def login(request):
    
    if request.method=="POST":
        
        name = request.POST['email']
        pWd = request.POST['password']
        val =Register.objects.filter(email=name, password=pWd).count()
        #data = Register.objects.all()
        if val == 1:
            request.session['email']=name
          
            return redirect('/', request.session['email'])
        else:
            messages.success(request,"Username and Passward wrong")
            return render(request,"login.html")

    else:
        return render(request,"login.html")



#logout

def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return redirect("/")

#forgetpassword
def forgetpassword(request):
     if request.method == "POST":
         
          val = Register.objects.filter(email=request.POST.get('emailll')).count()
          

          if val == 0:
                messages.success(request, 'Email is Not Register ...!')
                return render(request,'forgetpassword.html') 
          else:

                    with connection.cursor() as c:
                        email = request.POST.get('emailll')
                    
                        c.execute("Select password from register1 where email=%s ",[email])
                        myresult=c.fetchone()
                        for row in myresult:
                            # print(row)
                            #return HttpResponse(row)

                            subject = " ONLINE CV " 
                            msg     = "Your Email Address  :" + email + " Password : " + row + " "  
                            to      = email
                            res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
                            if(res == 1): 
                                messages.success(request, 'Your Email Addrese in Send Your Password!') 
                                #return   render(request,"login.html")
                               # msg = "Mail Sent Successfuly"
                        
                            else:  
                                    #msg = "Mail could not sent"
                                    messages.success(request, 'Mail could not sent!')   
                            return   render(request,"login.html")

                        #return HttpResponse(email)
                    return render(request,"forgetpassword.html")
     return render(request,"forgetpassword.html") 

#resumetips
def resumetips(request):
      return render(request,'resumetips.html')  


    
#insertform
def insertform(request):
    
    return render(request,'insertform.html')

#def profile
# global Reg_id
# def profile(request):
#       with connection.cursor() as cc:
#                         email =request.session['email']
                    
#                         cc.execute("Select id from register1 where email=%s ",[email])
#                         myresult=cc.fetchone()
                        
#                         for rowq in myresult:
                             
#                              Reg_id  = {'R_id':rowq}
#                              #return render(request,'profile.html',context)
#                              #return HttpResponse(context)
#                               #request.session['R_id'] = rowq
#                              return render(request,'profile.html',Reg_id)

#       return render(request,'profile.html')

context=0
def profile(request):
      with connection.cursor() as cc:
                        email =request.session['email']
                    
                        cc.execute("Select id from register1 where email=%s ",[email])
                        myresult=cc.fetchone()
                      
                        for rowq in myresult:
                           
                            global context
                            context  = {'R_id':rowq}
                            context = rowq
                            #return render(request,'profile.html',context)
                            return HttpResponse(context)
                              #request.session['R_id'] = rowq
                            


    

#insertreumeform
def insertpersonal(request):
    if request.method == "POST":
        psnl = Personal()
        p =  profile(request)
        psnl.R_id = context
        psnl.Fristname= request.POST.get('fname')
        psnl.secondname = request.POST.get('sname')
        psnl.lastname = request.POST.get('lname')
        psnl.title= request.POST.get('title')
        psnl.email = request.POST.get('email')
        psnl.mobile = request.POST.get('mobile')
        psnl.dob = request.POST.get('dob')
        psnl.gender = request.POST.get('gender')
        psnl.phone = request.POST.get('phone')
        psnl.linkedln = request.POST.get('addresslink')
        psnl.language = request.POST.get('language')
        if len(request.FILES) != 0:
            psnl.profilepicture = request.FILES['image']
        psnl.about = request.POST.get('about')
        psnl.address = request.POST.get('address')

      
        #R_id =  request.session['id'] ;

        

        
      
        psnl.save()
       
        return redirect('/Education')
        #return HttpResponse("Saved data",{'id':R_id})
    else:
      
        #return render(request,'PersonalDetails.html',{'id':R_id})
         return render(request,'PersonalDetails.html')
   






#insert Education details
def inserteducation(request):
    v =  profile(request)
    edu = Educationdetails.objects.all().filter(r_id=context)
    vi =  {'objec':edu}
    if request.method == "POST":
        prod = Educationdetails()
        p = profile(request)
        prod.r_id = context
        prod.qulification= request.POST.get('qulificaton')
        prod.college = request.POST.get('college')
        prod.board = request.POST.get('board')
        prod.year= request.POST.get('year')
        prod.percentageclass = request.POST.get('percentage')

        

        prod.save()
     
        #return redirect('/Experinace')
        return render(request,'Education.html',vi)
    else:
     return render(request,'Education.html',vi)
     
 #show fetchdata
# def showdata(request):
  
#     context1 = Item.objects.all()
#     cc = context
#     return render(request,'index.html',{'objec':cc})  

#show fetchdata
def showdata(request):
  
    context1 = Item.objects.all()
    
    return render(request,'index.html',{'objec':context1})






def experience(request) :
       v =  profile(request)
       edu = Experience.objects.all().filter(r_id=context)
       vi =  {'objec':edu}
       if request.method == 'POST' :
            exp = Experience()
            p = profile(request)
            exp.r_id = context
            exp.experience = request.POST['exp']
            exp.companyname = request.POST['Comapnayname']
            exp.startfrom = request.POST['startfrom']
            exp.startto = request.POST['startto']
            exp.programinglanguage = request.POST['ProgramingLanguage']
            exp.address = request.POST['workaddress']
            exp.role = request.POST['role']
            exp.save()
            
            return render(request,'Experinace.html',vi)

       else :
            return render(request,'Experinace.html',vi)          

def skills(request) :
       v =  profile(request)
       edu = Skills.objects.all().filter(r_id=context)
       vi =  {'objec':edu}
       if request.method == 'POST' :
            skls = Skills()
            p =  profile(request)
            skls.r_id = context
            skls.title = request.POST['subjectname']
            skls.rating = request.POST['marksrate']
            skls.save()
            
           # return render(request,'insertform.html')
            return render(request,'Experinace.html',vi)
       else :
            return render(request,'Skiles.html',vi)

def achivements(request):
        v =  profile(request)
        edu = Achievements.objects.all().filter(r_id=context)
        vi =  {'objec':edu}
        if request.method == 'POST' :
            achiv= Achievements()
            p =  profile(request)
            achiv.r_id = context
            achiv.title = request.POST['titleach1']
            achiv.descrption = request.POST['desc']
            achiv.save()
            return render(request,'Achievements.html',vi) 
        else :
            return render(request,'Achievements.html',vi)   


#download
def Download(request):
    return render(request,'Download.html')


#payment
   
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
def pay(request):
 

    order_amount = 50000
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
  

    payment_order =   client.order.create(dict(amount=order_amount, currency=order_currency    ))
    payment_order_id = payment_order['id']   
    context = {
        'amount':500,'api_key':RAZOR_KEY_ID,'order_id':payment_order_id
    } 
    return render(request,'pay.html',context)
                

def ii(request):
    return render(request,'ii.html')                      
     
     
   

#show data

def showEducaion(request):
      edu = Educationdetails.objects.all()
      return HttpResponse('Education.html',{'objec':edu})


#view Resume

def viewresume(request):


    p = profile(request)
    per =  Personal.objects.all().filter(R_id=context)
    edu = Educationdetails.objects.all().filter(r_id=context)
    exp = Experience.objects.all().filter(r_id=context)
    skil = Skills.objects.all().filter(r_id=context)
    ach = Achievements.objects.all().filter(r_id=context)

    con = {'objec':per,'vi':edu ,'exp':exp,'skil':skil,'ach':ach}
    return render(request,'viewresume.html',con)


def viewresumecopy(request):
     prl = Personal.objects.all()
     
     return render(request,'viewresumecopy.html',{'objec':prl})



