from django.db import models
import secrets
from django.db import IntegrityError

# Create your models here.


INVITE_CHOICES = ( 
    ("Wedding", "Wedding"), 
    ("Reception", "Reception"), 
) 
GENDER_CHOICES =(
    ("Mr. ","Male"),("Ms. ","Female"),
)

class Invitee(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    address = models.CharField(max_length=50)
    inviteStatus = models.CharField( max_length = 20, choices = INVITE_CHOICES, default = 'W')
    inviteeMessage = models.TextField(max_length=500,blank=True, default="You are cordially invited to the beautiful ceremony of my wedding. Your blessings matter the most to us!")
    siteVisited = models.BooleanField(default=False)
    secretCode = models.CharField(max_length=10, blank=True, editable=False, unique=True)

    # add index=True so we can look objects up by it
    # blank=True is so we can validate objects before saving - the save method will ensure that it gets a value

    def __str__(self):
        return self.name

    def URL(self):
        baseUrl="https://happycouples.herokuapp.com/rs/"
        return baseUrl+self.secretCode

    
    def save(self, *args, **kwargs):
        if not self.secretCode:
            self.secretCode =generateSecretCode()

            #self.secretCode = generate_random_alphanumeric(16)
            # using our function as above or anything else
        success = False
        failures = 0
        while not success:
            try:
                super(Invitee, self).save(*args, **kwargs)
            except IntegrityError:
                 failures += 1
                 if failures > 5: # or some other arbitrary cutoff point at which things are clearly wrong
                     raise
                 else:
                    # looks like a collision, try another random value
                    self.secretCode =secrets.token_hex(16)
                    #self.secretCode = generate_random_alphanumeric(16)
            else:
                 success = True


class Wisher(models.Model):
    # When we delete Invitee, then both Wisher and Invitee will be deleted.
    invitee = models.OneToOneField(Invitee,on_delete=models.CASCADE)
    wishes = models.CharField(max_length=500)
    posted = models.DateTimeField(auto_now=True)

    def Name(self):
        return self.invitee.name
    
    def Invitee(self):
        return self.invitee

def generateSecretCode():
    random = secrets.token_hex(16)
    # Get all the secretCodes to verify
    all= [obj.secretCode for obj in Invitee.objects.all()]
    if random in all:
        generateSecretCode()
    else:
        return random
