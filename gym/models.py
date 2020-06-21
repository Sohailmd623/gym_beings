from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=255,null=True)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=255, null=True)
    amount = models.FloatField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=255, null=True)
    member_id = models.CharField(max_length=255, null=True)
    contact = models.IntegerField(null=True, blank=True)
    alt_contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    plan = models.CharField(max_length=40)
    shifting = models.CharField(max_length=40, null=True)
    joining_date = models.DateField()
    expiry_date = models.DateField()
    initial_pay = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    unit = models.PositiveIntegerField()
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

