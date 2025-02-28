from django.db import models

# Create your models here.

class patient(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  email = models.EmailField()
  phone = models.CharField(max_length=150)
  message = models.TextField()
  date = models.DateField()

  def __str__(self):
    return self.name

class doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
      return self.name


class staff(models.Model):
  Fname = models.CharField(max_length=100)
  Lname = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  phonenumber = models.CharField(max_length=150)
  email = models.EmailField()
  Hiredate = models.DateField()

  def __str__(self):
    return self.Fname




class ward(models.Model):
    name = models.CharField(max_length=50)
    totalbeds = models.IntegerField()
    availablebeds = models.IntegerField()

    def __str__(self):
      return self.name


class appointment(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  phone= models.CharField(max_length=15)
  date = models.DateTimeField()
  department = models.CharField(max_length=50)
  doctor = models.CharField(max_length=50)
  message = models.TextField()

  def __str__(self):
    return self.name

class contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  subject = models.TextField()
  message = models.TextField()

  def __str__(self):
    return self.name

