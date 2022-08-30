from email.headerregistry import Address
from pickle import TRUE
from statistics import mode
import uuid
from django.db import models
from django.db.models import Q 
from users.models import MyUser

# Create your models here.
class Property(models.Model):
    landlord = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING)
    property_name = models.CharField(max_length=255, unique=True,null= False)
    address = models.CharField(max_length=35)
    county = models.CharField(max_length=35)
    number_of_units = models.PositiveIntegerField()
    property_type = models.CharField(max_length=35)
    units = models.PositiveIntegerField()
    property_image = models.ImageField(upload_to="propetry", null = TRUE)

    def __str__(self):
        return self.property_name
    
    @property
    def ownerID(self):
        return self.owner

    @staticmethod
    def get_property(name):
        return Property.objects.filter(
        Q(property_name__icontains=name) | Q(owner__first_name__icontains=name)
    )
