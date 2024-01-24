import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from indian_hero.models import indian
from apis.v1.serializers import heroSerializer
@csrf_exempt
def get_details(request):
    if request.method=='GET':
        result=indian.objects.all()
        serializer=heroSerializer(result,many=True)
        if serializer.is_valid:
            return JsonResponse(serializer.data,safe=False)
        else:
            return  HttpResponse("error occured")
    return HttpResponse("invalid details") 
@csrf_exempt    
def add_details(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        serializer=heroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    return HttpResponse("Invalid Request method")  
@csrf_exempt
def  edit_details(request):
    if request.method=="PATCH":
        data=JSONParser().parse(request)
        pk=data.get("id")
        obj=indian.objects.get(id=pk)
        serializer=heroSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    return HttpResponse("Invalid Request method") 
@csrf_exempt
def  put_details(request):
    if request.method=="PUT":
        data=JSONParser().parse(request)
        pk=data.get("id")
        obj=indian.objects.get(id=pk)
        serializer=heroSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    return HttpResponse("Invalid Request method")

@csrf_exempt
def  delete_details(request):
    if request.method=="DELETE":
        data=JSONParser().parse(request)
        pk=data.get("id")
        obj=indian.objects.get(id=pk)
        obj.delete()
        return HttpResponse("sucessfully deleted")
    else:   
        return HttpResponse("Invalid Request")