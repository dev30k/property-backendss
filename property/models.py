import uuid
from django.db import models
from django.db.models import Q 
from users.models import MyUser

# Create your models here.
class Business(models.Model):
    uuid =  models.UUIDField(primary_key = True,default = uuid.uuid4,
         editable = False)
    owner = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING)
    business_name = models.CharField(max_length=255, unique=True,null= False)
    payment_account_number = models.CharField(max_length=50,blank=False)
    property_description = models.TextField() 

    def __str__(self):
        return self.business_name
    
    @property
    def ownerID(self):
        return self.owner

    @staticmethod
    def get_property(name):
        return Business.objects.filter(
        Q(business_name__icontains=name) | Q(owner__first_name__icontains=name) | Q(uuid=name)
    )
