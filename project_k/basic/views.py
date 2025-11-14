from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student
from basic.models import post

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

def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})
    

@csrf_exempt
def addstudent(request):
    print(request.method)
    if request.method=="POST":
        data=json.loads(request.body)
        student=Student.objects.create(
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email")
            )
        return JsonResponse({"status":"success","id":student.id},status=200)
    
    elif request.method=="GET":
        result=list(Student.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)

    # elif request.method=="GET":
    #     data=json.loads(request.body)
    #     ref_id=data.get("id")
    #     result=Student.objects.filter(id=ref_id).values().first()
    #     return JsonResponse({"status":"ok","data":result},status=200)

    # elif request.method=="GET":
    #     data=json.loads(request.body)
    #     ref_age=data.get("age")
    #     result=list(Student.objects.filter(age__gte=ref_age).values())
    #     return JsonResponse({"status":"ok","data":result},status=200)

    # elif request.method=="GET":
    #     data=json.loads(request.body)
    #     ref_age=data.get("age")
    #     result=list(Student.objects.filter(age__lte=ref_age).values())
    #     return JsonResponse({"status":"ok","data":result},status=200)

    # elif request.method=="GET":
    #     result=list(Student.objects.order_by("name").values())
    #     return JsonResponse({"status":"ok","data":result},status=200)

    # elif request.method=="GET":
    #     result=list(Student.objects.values("age").distinct())
    #     return JsonResponse({"status":"ok","data":result},status=200)

    # elif request.method=="GET":
    #     result=Student.objects.count()
    #     return JsonResponse({"status":"ok","data":result},status=200)


    elif request.method=="PUT":
        data=json.loads(request.body)
        ref_id=data.get("id")  #getting id
        new_email=data.get("email")  #getting email
        existing_student=Student.objects.get(id=ref_id) #fetching the object as per the id
        existing_student.email=new_email #updating with new_email
        existing_student.save()
        updated_data=Student.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"data updated successfully","updated_Data":updated_data},status=200)
    
    elif request.method=="DELETE":
        data=json.loads(request.body)
        ref_id=data.get("id")
        get_delete_data=Student.objects.filter(id=ref_id).values().first()
        to_be_delete=Student.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"sucsess","message":"student data delete successfully","deleted_data":get_delete_data},status=200)
    return JsonResponse({"error":"use post method"},status=400)


@csrf_exempt
def addpost(request):
    if request.method=="POST":
        data=json.loads(request.body)
        posts=post.objects.create(
            post_name=data.get("post_name"),
            post_type=data.get("post_type"),
            post_date=data.get("post_date"),
            post_description=data.get("post_description")
        )
        return JsonResponse({"status":"success","id":posts.id},status=200)
    
    elif request.method=="GET":
        result=list(post.objects.values())
        return JsonResponse({"status":"ok","result":result},status=200)
    
    elif request.method=="PUT":
        data=json.loads(request.body)
        ref_id=data.get("id")
        new_post_type=data.get("post_type")
        present_data=post.objects.get(id=ref_id)
        present_data.post_type=new_post_type
        present_data.save()
        updated_data=post.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"ok","result":updated_data},status=200)
    
    elif request.method=="DELETE":
        data=json.loads(request.body)
        ref_id=data.get("id")
        get_delete_data=post.objects.filter(id=ref_id).values().first()
        to_be_delete=post.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"sucsess","message":"student data delete successfully","deleted_data":get_delete_data},status=200)
    return JsonResponse({"error":"use post method"},status=400)
