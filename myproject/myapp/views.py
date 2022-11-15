
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse
from .forms import StudentForm

# Create your views here.

def Student(request):
     
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student.html', {'Student': Student})
    else :
        form =StudentForm()
    return  render(request,'student.html',{'form':form})
 
#    