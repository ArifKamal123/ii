# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User





class Customer(models.Model):
    pass_id = models.CharField(primary_key=True, max_length=20)
    address = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    package = models.ForeignKey('Packages', models.DO_NOTHING, blank=True, null=True)
    depart_date = models.DateField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    depart_origin = models.CharField(max_length=50, blank=True, null=True)
    arrival_origin = models.CharField(max_length=50, blank=True, null=True)
    depart_origin_1 = models.CharField(max_length=50, blank=True, null=True)
    arrival_origin_1 = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'customer'
    
    def __str__(self):
        return self.name



class Hotels(models.Model):
    hotel_id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    bed_type = models.CharField(max_length=10, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    per_night = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hotels'
    
    def __str__(self):
        return self.name


class Packages(models.Model):
    package_id = models.DecimalField(primary_key=True, max_digits=1, decimal_places=0)
    hotel = models.ForeignKey(Hotels, models.DO_NOTHING, blank=True, null=True,related_name='hotel_ID')
    name = models.CharField(max_length=50, blank=True, null=True)
    days = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    makkah_days_1 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    madina_days = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ziyarat = models.BooleanField(blank=True, null=True)
    food = models.FloatField(blank=True, null=True)
    makkah_days_2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    hotel_madina = models.ForeignKey(Hotels, models.DO_NOTHING, db_column='hotel_madina', blank=True, null=True,related_name='hotel_madina')

    class Meta:
        managed = True
        db_table = 'packages'
    
    def __str__(self):
        return self.name
