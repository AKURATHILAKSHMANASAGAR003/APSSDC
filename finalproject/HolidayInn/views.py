from django.shortcuts import render,redirect
from django.http import HttpResponse
from HolidayInn.forms import Usregis,Upd,Pad,Rms
from finalproject import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from HolidayInn.models import Exfd,Room

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			sb = "Testing Email to register for Hoilday INN"
			mg = "Hi Welcome {} you have successfully registered in our portal with password : {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for Login Credentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"Please enter correct Mail Id (or) Username (or) Password")

	y = Usregis()
	return render(request,'html/register.html',{'t':y})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def prfle(request):
	return render(request,'html/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd)
		if p.is_valid and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'html/updateprofile.html',{'r':p,'q':t})

@login_required
def roms(request):
	p = Room.objects.filter(m_id=request.user.id)
	print(p)
	return render(request,'html/room.html',{'y':p})

@login_required
def creationwk(request):
	if request.method == "POST":
		r = Rms(request.POST)
		if r.is_valid():
			t = r.save(commit=False)
			t.m_id = request.user.id
			t.save()
			messages.success(request,"Successfully Booked your Room..! For Further Information Contact our People in Information Page / Footer..")
			return redirect('/pf')
	r = Rms()
	return render(request,'html/crwrk.html',{'d':r})
