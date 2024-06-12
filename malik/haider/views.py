from datetime import datetime
from email.headerregistry import Address

from django.shortcuts import render,HttpResponse
from django.contrib import messages
from haider.models import Contact,Feedback,Home
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import Contactserializer, Feedbackserializer, Homeserializer
from rest_framework.decorators import api_view
from rest_framework import status




# Create your views here.
def index(request):
    return render(request,'index.html')

def details(request):
    return render(request,'details.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        foz=Contact(name=name,phone=phone,email=email,message=message)
        foz.save()
    return render(request,'contact.html')

def feedback(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        taste=request.POST.get('taste')
        whatsnew=request.POST.get('whatsnew')
        change=request.POST.get('change')
        fiza=Feedback(name=name,phone=phone,email=email,taste=taste,whatsnew=whatsnew,changes=change)
        fiza.save()
    return render(request,'feedback.html')

def home(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        mainarea=request.POST.get('mainarea')
        subarea=request.POST.get('subarea')
        streetno=request.POST.get('streetno')
        flavour=request.POST.get('flavour')
        topping=request.POST.get('topping')
        instructions=request.POST.get('instructions')
        taiba=Home(name=name,phone=phone,address=address,topping=topping,mainarea=mainarea,subarea=subarea,streetno=streetno,flavour=flavour,instructions=instructions)
        taiba.save()
    return render(request,'index.html')

#Contact APi
@api_view(['GET','POST'])
def contact_api(request):
    if request.method=='GET':
        foz=Contact.objects.all()
        serializer=Contactserializer(foz,many=True)
        return Response(serializer.data)
    #CREATE
    if request.method=='POST':
        serializer=Contactserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


#Contact APi CRUD methods
@api_view(['GET','POST','PUT','DELETE'])
def contact_detail(request,id):
    try:
        foz=Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #READ
    if request.method=='GET':
        serializer=Contactserializer(foz)
        return Response(serializer.data)
    #CREATE
    if request.method=='POST':
        serializer=Contactserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    #update
    if request.method=='PUT':
        serializer=Contactserializer(foz,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method=='DELETE':
        foz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Feedback APi CRUD methods
@api_view(['GET','POST'])
def Feedback_api(request):
    if request.method=='GET':
        fiza=Feedback.objects.all()
        serializer=Feedbackserializer(fiza,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=Feedbackserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
#CRUD FEEDBACK API
@api_view(['GET','PUT','POST','DELETE'])
def Feedback_detail(request,id):
    try:
        fiza=Feedback.objects.get(pk=id)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    #READ
    if request.method=='GET':
        serializer=Feedbackserializer(fiza)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    #UPDATE
    if request.method=='PUT':
        serializer=Feedbackserializer(fiza,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #POST
    if request.method=='POST':
        serializer=Feedbackserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    if request.method=='DELETE':
        fiza.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


#Home Api
@api_view(['GET','POST'])
def Home_api(request):
    if request.method=='GET':
        foz=Home.objects.all()
        serializer=Homeserializer(foz,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=='POST':
        serializer=Homeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
#crud methods Homeapi
@api_view(['GET','PUT','POST','DELETE'])
def Home_detail(request,id):
    try:
        foz=Home.objects.get(pk=id)
    except Home.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #read
    if request.method=='GET':
        serializer=Homeserializer(foz)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    #update
    if request.method=='PUT':
        serializer=Homeserializer(foz,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    #create
    if request.method=='Post':
        serializer=Homeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    #Delete
    if request.method=='DELETE':
        foz.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


















