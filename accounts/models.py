from django.db import models

# Create your models here.
class PatientInfo(models.Model):
    date = models.CharField(max_length=255)
    clinic = models.CharField(max_length=255)

    lname = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)

    address = models.TextField()

    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

    phone = models.CharField(max_length=255)
    ssecurity = models.CharField(max_length=255)

    dob = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    mstatus = models.CharField(max_length=255)
    dlicense = models.CharField(max_length=255)
    wphone = models.CharField(max_length=255)

    ena = models.TextField()
    email = models.CharField(max_length=255)
    eca = models.CharField(max_length=255)
    ecd = models.CharField(max_length=255)

    heardby = models.CharField(max_length=255)
    refferedby = models.CharField(max_length=255)

    def __str__(self):
        return self.email
# class GuanratorInfo(models.Model):
#
#     patient_id = models.ForeignKey(PatientInfo,on_delete=models.CASCADE)
#     relationgtop = models.CharField(max_length=255)
#
#     lname = models.CharField(max_length=255)
#     fname = models.CharField(max_length=255)
#     mname = models.CharField(max_length=255)
#
#     address = models.TextField()
#
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     zip = models.CharField(max_length=255)
#
#     phone = models.CharField(max_length=255)
#     ssecurity = models.CharField(max_length=255)
#
#     dob = models.CharField(max_length=255)
#     age = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255)
#     ena = models.TextField()

    def __str__(self):
        return self.email