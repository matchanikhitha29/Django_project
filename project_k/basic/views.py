from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse("hello world!")

def shopping(request):
    data={"brand":"clothing"}
    return JsonResponse(data)

def sampleInfo(request):
    data=[1,2,3,4]
    return JsonResponse(data,safe=False)

def dynamicResponse(request):
    name=request.GET.get("name",'')
    city=request.GET.get("city",'hyd')
    return HttpResponse(f"hello {name} from {city}")

def sum(request):
    num1=request.GET.get("num1",'')
    num2=request.GET.get("num2",'')
    num1=int(num1)
    num2=int(num2)
    return HttpResponse({num1+num2})

def subtract(request):
    return HttpResponse(20-10)