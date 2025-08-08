from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CNUser(AbstractUser):

    ## Atributes ##
    CNUsername = models.CharField(max_length=50, blank=False, null=False)
    CNBio = models.TextField(null=False, blank=True)
    CNPicture = models.FileField(null=False, blank=True)
    CNBirthdate = models.DateField(null=False, blank=False)
    CNEmail = models.CharField(max_length=50, blank=False, null=False)
    ###############

    ## Functions ##
    @classmethod
    def createNewUser(cls, username, birthdate, email, password):
        return cls.objects.create_user(CNUsername=username, CNBirthdate=birthdate, CNEmail=email, username=username, email=email, password=password)
    ###############