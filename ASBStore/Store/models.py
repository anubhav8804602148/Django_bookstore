from django.db import models 


class Book(models.Model):
  book_id=models.IntegerField()
  name=models.CharField(max_length=50)
  author=models.CharField(max_length=20)
  published_in=models.DateField()
  status=models.CharField(max_length=3)
  owner=models.CharField(max_length=20)

class User(models.Model):
  user_id=models.IntegerField()
  fname=models.CharField(max_length=20)
  lname=models.CharField(max_length=20)
  dob=models.DateField()
  gender=models.CharField(max_length=1)
