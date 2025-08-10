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
    
    @classmethod
    def updateInfos(cls, id, username, bio, picture):

        ## Profile ##
        profile = cls.objects.get(id=id)

        ## Updating infos ##
        profile.CNUsername = username
        profile.CNBio = bio
        profile.CNPicture = picture
        profile.username = username

        ## Saving the data
        profile.save()

    ###############

class Post(models.Model):

    ## Atributes ##
    title = models.CharField(max_length=55, null=False, blank=False)
    content = models.TextField(null=False, blank=True)
    attachment = models.FileField(null=False, blank=True)
    userOwner = models.ForeignKey(CNUser, on_delete=models.CASCADE)
    likes = models.IntegerField(null=False, blank=False, default=0)

    ################

    ## Functions ##
    @classmethod
    def newPost(cls, title, content, attachment, userOwner):

        ## If for attachment == 1 ##
        if attachment != "":
            return cls.objects.create(title=title, content=content, attachment=attachment, userOwner=userOwner)
        
        ## Elif for attachment == 0
        elif attachment == "":
            return cls.objects.create(title=title, content=content, userOwner=userOwner)
        
class PostLike(models.Model):

    ## Atributes ##
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    userOwner = models.ForeignKey(CNUser, on_delete=models.CASCADE)

    ###############

    ## Functions ##
    @classmethod
    def giveLike(cls, post, userOwner):
        return cls.objects.create(post=post, userOwner=userOwner)
    
    @classmethod
    def unLike(cls, post, userOwner):
        return cls.objects.get(post=post, userOwner=userOwner).delete()