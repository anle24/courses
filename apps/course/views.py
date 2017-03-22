from django.shortcuts import render, redirect
from .models import Course, Description

# Create your views here.
def index(request):
    context = {
    "descriptions": Description.objects.all()
    }
    return render(request, "course/index.html", context)

def addCourse(request):
    course = Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'], course=course)
    return redirect('/')

def removeCourse(request, id):
    course = Course.objects.get(id=id)
    context ={
    "course": course,
    "description": Description.objects.get(course=course)
    }
    return render(request, "course/remove.html", context)

def delete(request, id):
    course = Course.objects.filter(id=id)
    Description.objects.filter(course=course).delete()
    course.delete()
    return redirect('/')
