from django.shortcuts import render
from . models import Mango
from django . http import JsonResponse
from . serializer import Bioserializer
from rest_framework.decorators import api_view
@api_view(["GET","POST"])
def index(request):
    if request.method=='GET':
        Bio=Mango.objects.all()
        ser=Bioserializer(Bio,many=True)
        return JsonResponse(ser.data,safe=False)
    elif request.method=='POST':
         ser=Bioserializer(data=request.data)
         if ser.is_valid():
             ser.save()
         return JsonResponse(ser.data,safe=False)
    return JsonResponse()
def details(request,id):
    try:
        Bio=Mango.objects.get(pk=id)
    except Mango.Doesnotexit:
        return JsonResponse({'error':'Data not found'})
    ser=Bioserializer(Bio)
    return JsonResponse(ser.data,safe=False)
    
        


