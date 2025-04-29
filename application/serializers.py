# tis file if used for converting the comlex data to simple python object for showing the data through the api 
# data we have to show to the other party we need to serialize that data in this file 

from rest_framework import serializers

class contact_tableSerializers(serializers.Serializer):
    name=serializers.CharField(max_length =100)
    email=serializers.CharField(max_length=100)
    phone =serializers.CharField(max_length=10)
    enquiry = serializers.CharField(max_length=30)

class book_tableSerializers(serializers.Serializer):
    name=serializers.CharField(max_length =100)
    email=serializers.CharField(max_length=100)
    phone =serializers.CharField(max_length=10)
    date=serializers.DateField()
    reservation=serializers.CharField(max_length=100)

class event_Serializers(serializers.Serializer):
    name=serializers.CharField(max_length =100)
    email=serializers.CharField(max_length=100)
    phone =serializers.CharField(max_length=10)
    date=serializers.DateField()
    eventname = serializers.CharField(max_length=50)
    reservation=serializers.CharField(max_length=100)