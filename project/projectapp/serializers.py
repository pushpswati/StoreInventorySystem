from rest_framework import serializers
from projectapp.models import StoreUser
from projectapp.models import InventoryRecord
class StoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=StoreUser
        fields=('created','username','email','password','is_manager','is_assistant')


class InventoryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryRecord
        fields=('created','product_id','product_name','user_id','is_approve')
