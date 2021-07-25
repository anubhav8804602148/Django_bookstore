from django.db import models 

class Book(models.Model):
  #book_id=models.IntegerField()
  name=models.CharField(max_length=50,default=" ")
  #author=models.CharField(max_length=20,blank=False,default="LIB")
  #published_in=models.DateField(blank=False,default="01-01-1990")
  #status=models.CharField(max_length=3,blank=False,default="AVL")
  #owner=models.CharField(max_length=20,blank=False,default="LIB")

class User(models.Model):
  #user_id=models.IntegerField()
  fname=models.CharField(max_length=20,default=" ")
  #lname=models.CharField(max_length=20,blank=False,default=" ")
  #dob=models.DateField(blank=False, default="01-01-1990")
  #gender=models.CharField(max_length=1,blank=False,default="M")



 