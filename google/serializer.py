from rest_framework import serializers
from .models import Mango

class Bioserializer(serializers.ModelSerializer):
    class Meta:
        model=Mango
        fields =['id','name','age','phone','email','address']
