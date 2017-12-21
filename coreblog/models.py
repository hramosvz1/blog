#!/usr/bin/python
# -*- coding: utf-8    -*-
import os, sys
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.



class User(models.Model):
     Username= models.CharField(max_length=30)
     First_N=models.CharField(max_length=50)
     Last_N=models.CharField(max_length=50)
     Password = models.CharField(max_length=30)

     def __str__(self):
     	return self.Username

class Post(models.Model):
     Title= models.CharField(max_length=100)
     Content= models.TextField(max_length=3000)
     Category= models.ManyToManyField('Category', blank=True) 
     Author=models.ForeignKey('User',on_delete=models.CASCADE,)
     Image=  models.ImageField(upload_to = 'post_head_img', default='')
     Timestamp = models.DateTimeField(auto_now= False, auto_now_add=True)
     Updated = models.DateTimeField(auto_now= True, auto_now_add=False)
     
     def __str__(self):
        return self.Title

class Category(models.Model):
     Name= models.CharField(max_length=50)
     Image=models.ImageField(upload_to = 'category_head_img', default='')
     
     def __str__(self):
        return self.Name
