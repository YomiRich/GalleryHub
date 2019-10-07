from django.shortcuts import render,redirect
from .models import Location,Image
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def photo_of_day(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'todayphoto.html',{"images":images, "location": location})
