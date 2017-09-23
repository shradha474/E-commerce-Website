from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):

    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    image_pic  =models.FileField( upload_to='images/latest')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_skirts(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    skirts_pic = models.FileField( upload_to='images/latest')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_watch(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    watch_pic = models.FileField( upload_to='images/latest')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_dress(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    dress_pic = models.FileField( upload_to='images/dress')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_sweaters(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    sweaters_pic = models.FileField( upload_to='images/sweaters')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_jeans(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    jeans_pic = models.FileField( upload_to='images/jeans')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_shirts(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    shirts_pic = models.FileField( upload_to='images/shirts')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_salwar(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    salwar_pic = models.FileField( upload_to='images/salwar')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_sarees(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    sarees_pic = models.FileField( upload_to='images/sarees')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_products(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    product_pic = models.FileField( upload_to='images/product')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_footwear(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    footwear_pic = models.FileField( upload_to='images/footwear')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class checkout(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField( upload_to='images/checkout')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title

class Index_kids(models.Model):
    Description = models.CharField(max_length=2500)
    image_title = models.CharField(max_length=500)
    amount =  models.DecimalField(max_digits=6, decimal_places=2)
    kids_pic = models.FileField( upload_to='images/kids')
##    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.image_title + ' - ' + self.image_title
