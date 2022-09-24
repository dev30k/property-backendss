from email.headerregistry import Address
from pickle import TRUE
from statistics import mode
import uuid
from django.db import models, IntegrityError
from django.db.models import Q
from users.models import MyUser
from django import forms


# Create your models here.
class Property(models.Model):
    property_types_options = [
        ('C', 'commercial'),
        ('R', 'Residential'),
    ]

    property_name = models.CharField(max_length=255, unique=True, null=False)
    address = models.CharField(max_length=35)
    county = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    zipcode = models.PositiveBigIntegerField()
    property_type = models.CharField(max_length=5, choices=property_types_options)
    landlord = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    property_image = models.ImageField(upload_to="propetry", null=TRUE)

    class meta:
        unique_together = ['property_name', 'address', 'county']
        groupby = unique_together

    def __str__(self):
        return self.property_name

    @property
    def ownerID(self):
        return self.owner

    @staticmethod
    def get_property(name):
        return Property.objects.filter(
            Q(property_name__icontains=name) | Q(landlord__first_name__icontains=name)
        )


class ResidentailProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_type = models.CharField(max_length=35, null=False)
    market_rent = models.PositiveIntegerField(blank=False)
    beds = models.PositiveIntegerField(blank=False)
    square_feet = models.FloatField(null=False, blank=False)
    number_of_units = models.PositiveIntegerField(blank=False)

    # care_taker TODO: creat care taker table

    def clean(self, *args, **kwargs):
        try:
            if not self.property_name.property_type == 'R':
                raise forms.ValidationError({'property_name': ["propety type not residental"]})
            else:
                super().save(*args, **kwargs)
        except IntegrityError as e:
            raise forms.ValidationError(message=e.msg)

    def __str__(self) -> str:
        return self.property_name.property_name


class CommercialProperty(models.Model):
    square_feet = models.FloatField(null=False, blank=False)
    price_per_squre_foot = models.PositiveIntegerField(blank=False)
    Type = models.CharField(max_length=35, null=False)
    property_name = models.ForeignKey(Property, on_delete=models.CASCADE)

    def clean(self, *args, **kwargs):
        try:
            if not self.property_name.property_type == 'C':
                raise forms.ValidationError({'property_name': ["propety type not commercial"]})
            else:
                super().save(*args, **kwargs)
        except IntegrityError as e:
            raise forms.ValidationError(message=e.msg)

    def __str__(self) -> str:
        return self.property_name.property_name
