from django.db import models
from django.urls import reverse
from django.conf.urls import url
from django import forms

class Voter(models.Model):
	name = models.CharField(max_length=150)
	rolno = models.CharField(max_length=150)
	Username = models.CharField(max_length=150)
	Password = models.CharField(max_length=150)
	cashing = models.IntegerField(null=True,default=0)
	candidate = models.IntegerField(null=True,default=0)

	def get_absolute_url(self):
		return reverse("voting:voter-detail", kwargs={"id": self.id})


class Candidate(models.Model):
	name = models.CharField(max_length=150)
	rolno = models.CharField(max_length=150)
	symbol = models.ImageField(upload_to='symbols/',max_length=225,null=True)
	votes = models.IntegerField(null=True,default=0)

	def get_absolute_url(self):
		return reverse("voting:candi-detail", kwargs={"id": self.id})

