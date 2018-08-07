
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
           

class AddInventoryRecord(APIView):
      def post(self,request,format=None):
          product_id = request.data['product_id']
          product_name = request.data['product_name']
          vender = request.data['vender']
          mrp = request.data['mrp'] 
          user_id = request.data['user_id']
          batch_num = request.data['batch_num']
          batch_date = request.data['batch_date']
          quantity = request.data['quantity']
          is_approve = request.data['is_approve']
          
          # select query in orm
          inventory_obj = Storeuser.objects.get(email=email)
          
          user_obj = StudentEnroll.objects.create(product_id=product_id, product_name=product_name, user_id=user_id)
          msg_response = "Inventory add Successfully"

                 # Custom response dict
          response_dict={"user_id":str(user_id),
                         "product_id":str(product_id),
                         "response":msg_response}

                 # Final rensponse to send
          RESPONSE={"success":True,
                           "response":response_dict}

          return Response(RESPONSE, status=status.HTTP_201_CREATED)

          
          msg_response = "This Course id alraeady exceed limit of students, Please select"

             # Final rensponse to send
          RESPONSE = {"success": True,
                         "response": msg_response}
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Approve(APIView):
      def post(self,request,format=None):
          email = request.data['email']
          is_manager = request.data['is_manager']
          inventory_obj = StoreUser.objects.get(email=email)
          if inventory_obj.is_manager==True: 
                       in_obj = InventoryRecord.objects.filter(is_approve=False)
                       print(in_obj)  
                       serializer = InventoryRecordSerializer(in_obj,many=True)
          return Response(serializer.data, status=status.HTTP_201_CREATED)


      


