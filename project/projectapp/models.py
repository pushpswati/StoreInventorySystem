from __future__ import unicode_literals
from django.db import models

class StoreUser(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      username = models.CharField(max_length=100, blank=True)
      password = models.CharField(max_length=10)
      is_manager = models.BooleanField(default='False')
      is_assistant = models.BooleanField(default='False')
      email = models.EmailField()
      
      class Meta:
          ordering = ('created',)

class InventoryRecord(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      user_id = models.CharField(max_length=100,blank=True,default='')
      product_id = models.CharField(max_length=100)
      product_name = models.CharField(max_length=100,blank=True,default='')
      vender_name = models.CharField(max_length=100,blank=True,default='')
      mrp = models.CharField(max_length=100,blank=True,default='')
      batch_num = models.CharField(max_length=100)
      batch_date = models.CharField(max_length=100,blank=True,default='')
      quantity = models.CharField(max_length=100,blank=True,default='')
      is_approve = models.BooleanField(default='False')
      

      class Meta:
          ordering = ('created',)
 
