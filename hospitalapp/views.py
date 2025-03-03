from django.shortcuts import render,redirect
from hospitalapp.models import *


# Create your views here.


def index(request):
  return render(request,'index.html')


def service(request):
  return render(request,'service-details.html')

def starter(request):
  return render(request,'starter-page.html')


def about(request):
  return render(request,'about.html')


def services(request):
  return render(request,'services.html')

def departments(request):
  return render(request,'departments.html')

def doctors(request):
  return render(request,'doctors.html')

def appoint(request):
  return render(request,'appointment.html')

def appoint(request):
   if request.method == "POST":
     myappointments = appointment(
       name = request.POST['name'],
       email = request.POST['email'],
       phone = request.POST['phone'],
       date = request.POST['date'],
       department = request.POST['department'],
       doctor = request.POST['doctor'],
       message = request.POST['message'],
     )
     myappointments.save()
     return redirect('/show')
   else:
     return render(request,'appointment.html')


def contacts(request):
  return render(request,'contact.html')


def contacts(request):
  if request.method == "POST":
    mycontacts = contact(
      name=request.POST['name'],
      email=request.POST['email'],
      subject=request.POST['subject'],
      message=request.POST['message']
     )
    mycontacts.save()
    return redirect('/contact')
  else:
    return render(request,'contact.html')


def show(request):
    all =appointment.objects.all()
    return render(request,'show.html',{'all':all})

def delete(request,id):
 deleteappointment = appointment.objects.get(id=id)
 deleteappointment.delete()
 return redirect('/show')

