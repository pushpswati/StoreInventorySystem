from projectapp.models import StoreUser
from projectapp.models import InventoryRecord
from projectapp.serializers import InventoryRecordSerializer
from projectapp.serializers import StoreUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User




class StoreSingup(APIView):
 
    

     def post(self, request, format=None):
        serializer = StoreUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreLogin(APIView):
     
      # This is login api
      def post(self,request, format=None):
          print("Checkpoint 1")
          serializer = StoreUserSerializer(data=request.data)
          email = request.data['email']
          #print("Checkpoint 2 l",email)
          passwd = request.data['password']
          print("Checkpoint 3 password==",passwd)

          # Write your code for check email sssst in db
          try:
              user = StoreUser.objects.get(email=email)
         
              if user is not None:
                  if user.password==passwd:
                      print("Login successfull: ",)

                      #token

                      return Response({"sucess":"true","message":"Loging successfull"}, status=status.HTTP_200_OK)
                  else:
                      return Response({"sucess":"false","message":"Login not successfull"}, status=status.HTTP_400_BAD_REQUEST)

              else:
                  return Response({"sucess":"false","message":"Login not successfull"}, status=status.HTTP_400_BAD_REQUEST)

          except:
              return Response({"sucess":"false","message":"Mail does not exist"}, status=status.HTTP_400_BAD_REQUEST)

class Inventorylist(APIView):
      def get(self,request,format=None):
          print("checkpoint 1")
          Inventory_obj = InventoryRecord.objects.all()
          serializer = InventoryRecordSerializer(Inventory_obj,many=True)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
           
class Userlist(APIView):
      def get(self,request,format=None):
          print("checkpoint 1")
          Inventory_obj = StoreUser.objects.all()
          serializer = StoreUserSerializer(Inventory_obj,many=True)
          return Response(serializer.data, status=status.HTTP_201_CREATED)






class AddInventoryRecord(APIView):
      def post(self,request,format=None):
          product_id = request.data['product_id']
          product_name = request.data['product_name']
          email = request.data['email']



          
          # select query in orm
          user_obj = StoreUser.objects.get(email=email)
          user_id=user_obj.id
          inventry_obj = InventoryRecord.objects.create(product_id=product_id, product_name=product_name, user_id=user_id)
          msg_response = "Inventory add Successfully"

                 # Custom response dict
          response_dict={"user_id":str(user_id),
                         "product_id":str(inventry_obj.product_id),
                         "response":msg_response}

                 # Final rensponse to send
          RESPONSE={"success":True,
                           "response":response_dict}

          return Response(RESPONSE, status=status.HTTP_201_CREATED)

          
         
class Approve(APIView):
      def post(self,request,format=None):
          email = request.data['email']

          user_obj = StoreUser.objects.get(email=email)
          if user_obj.is_manager==True: 
                       inies_obj = InventoryRecord.objects.filter(is_approve=False)
                       print(inies_obj) 
                       inventry_id_list=[i.id for i in inies_obj] # List of Inventries Ids #using list comprehension
                       for j in inventry_id_list:
                           invetry_obj=InventoryRecord.objects.get(id=j)# get particular inventry id obj
                           invetry_obj.is_approve=True
                           invetry_obj.save()
                       print(inventry_id_list)
                       serializer = InventoryRecordSerializer(inies_obj,many=True)
          return Response(serializer.data, status=status.HTTP_201_CREATED)


      


