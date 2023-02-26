from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import student
# Create your views here.
def add(request):
  form=StudentForm(request.POST or None)
  #student=student.objects.all()
  if form.is_valid():
     form.save()
       
  return render(request,'add.html',{'form':form})
def show(request):
  std=student.objects.all()
  return render(request,'show.html',{'student':std})
def update(request,id):
  std=student.objects.get(id=id)
  form=StudentForm(request.POST,instance=std)
  if form.is_valid():
     form.save()
     return HttpResponseRedirect('/')
  return render(request,'update.html',{'student':std})

def delete(request,id):
  form=student.objects.get(id=id)
  form.delete()
  return HttpResponseRedirect('/')
    
