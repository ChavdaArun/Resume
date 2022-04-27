from django.urls import path
from  demo import views

urlpatterns = [
path("",views.index,name='home'),

#show data
path("AddResume",views.AddResume,name='AddResume'),
path("showdata",views.showdata,name='showdata'),

#register
path("register",views.register,name='register'),

#Login
path("login",views.login,name='login'),

#foregetpassword
path("forgetpassword",views.forgetpassword,name='forgetpassword'),

#logout
path("logout",views.logout,name='logout'),

#profile
path("profile",views.profile,name='profile'),

#resumetips
path("resumetips",views.resumetips,name='resumetips'),

#insertforms
#path("insertform",views.insertform,name='insertform'),



#personal details

#path("PersonalDetails/<int:R_id>",views.insertpersonal,name='PersonalDetails'),

path("PersonalDetails",views.insertpersonal,name='PersonalDetails'),

#education details
path("Education",views.inserteducation,name='Education'),

#experience details
path("Experinace",views.experience,name='Experinace'),

#skiles details
path("Skiles",views.skills,name='Skiles'),

#Achievements details
path("Achievements",views.achivements,name='Achievements'),

#download
path("Download",views.Download,name='Download'),


#payment
path("pay",views.pay,name='pay'),


path("ii",views.ii,name='ii'),


#viewResume
path("viewresume",views.viewresume,name='viewresume'),
path("viewresumecopy",views.viewresumecopy,name='viewresumecopy'),


]

