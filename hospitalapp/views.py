from django.shortcuts import render,redirect,get_object_or_404
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

def edit(request,id):
  appointment1= get_object_or_404(appointment,id=id)
  if request.method == 'POST':
    appointment1.name = request.POST.get('name')
    appointment1.email = request.POST.get('email')
    appointment1.phone = request.POST.get('phone')
    appointment1.date = request.POST.get('date')
    appointment1.department = request.POST.get('department')
    appointment1.doctor = request.POST.get('doctor')
    appointment1.message = request.POST.get('message')
    appointment1.save()
    return redirect('/show')

  else:
    return render(request,'edit.html',{'appointment1':appointment1})

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

