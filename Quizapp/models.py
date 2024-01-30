from django.db import models

# Create your models here.


class NewUser(models.Model):
    user_name = models.CharField(max_length=50,null=True)
    
# Sports Questions
class SportsQuestion(models.Model):
    catagery = models.CharField(max_length=50,null=True,default='Sports')
    question_no = models.IntegerField(null=True)
    question = models.TextField(max_length=500,null=True)
    opt1 = models.CharField(max_length=80,null=True)
    opt2 = models.CharField(max_length=80,null=True)
    opt3 = models.CharField(max_length=80,null=True)
    opt4 = models.CharField(max_length=80,null=True)
    correct_opt = models.CharField(max_length=80,null=True)
    related_img = models.ImageField(upload_to="questions/related_images/sports",null=True)

# Plantss and Animal Questions
class PlantsAndAnimalQuestion(models.Model):
    catagery = models.CharField(max_length=50,null=True,default='Plants_and_cuAnimal')
    question_no = models.IntegerField(null=True)
    question = models.TextField(max_length=500,null=True)
    opt1 = models.CharField(max_length=80,null=True)
    opt2 = models.CharField(max_length=80,null=True)
    opt3 = models.CharField(max_length=80,null=True)
    opt4 = models.CharField(max_length=80,null=True)
    correct_opt = models.CharField(max_length=80,null=True)
    related_img = models.ImageField(upload_to="questions/related_images/plants_and_animal",null=True)
   
# Zoology Questions
class ZoologyQuestion(models.Model):
    catagery = models.CharField(max_length=50,null=True,default='Zoology')
    question_no = models.IntegerField(null=True)
    question = models.TextField(max_length=500,null=True)
    opt1 = models.CharField(max_length=80,null=True)
    opt2 = models.CharField(max_length=80,null=True)
    opt3 = models.CharField(max_length=80,null=True)
    opt4 = models.CharField(max_length=80,null=True)
    correct_opt = models.CharField(max_length=80,null=True)
    related_img = models.ImageField(upload_to="questions/related_images/zoology",null=True)

# History Questions   
class HistoryQuestion(models.Model):
    catagery = models.CharField(max_length=50,null=True,default='History')
    question_no = models.IntegerField(null=True)
    question = models.TextField(max_length=500,null=True)
    opt1 = models.CharField(max_length=80,null=True)
    opt2 = models.CharField(max_length=80,null=True)
    opt3 = models.CharField(max_length=80,null=True)
    opt4 = models.CharField(max_length=80,null=True)
    correct_opt = models.CharField(max_length=80,null=True)
    related_img = models.ImageField(upload_to="questions/related_images/history",null=True)
  
# Current Affairs Questions
class CurrentAffairsQuestion(models.Model):
    catagery = models.CharField(max_length=50,null=True,default='Current_Affairs')
    question_no = models.IntegerField(null=True)
    question = models.TextField(max_length=500,null=True)
    opt1 = models.CharField(max_length=80,null=True)
    opt2 = models.CharField(max_length=80,null=True)
    opt3 = models.CharField(max_length=80,null=True)
    opt4 = models.CharField(max_length=80,null=True)
    correct_opt = models.CharField(max_length=80,null=True)
    related_img = models.ImageField(upload_to="questions/related_images/current_affairs",null=True)
    
# User Results
class UserResult(models.Model):
    user_id = models.BigIntegerField(null=True)
    user_name = models.CharField(max_length=50,null=True)
    score = models.IntegerField(null=True)
    
# User Feeddback
class Feedback(models.Model):
    user_id = models.BigIntegerField(null=True) 
    user_name = models.CharField(max_length=50,null=True)
    feedback = models.CharField(max_length=50,null=True)