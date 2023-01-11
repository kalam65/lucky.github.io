from django.shortcuts import render,redirect
from curdapp.models import Employees

# Create your views here.
def Register_app(request):
    emp=Employees.objects.all()
    
    context={
        'emp':emp,
        
    }
    
    
    return render(request,"base.html",context)

def add(request):
    
    if request.method == "POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Address=request.POST.get('Address')
        Phone=request.POST.get('Phone')
        
        emp=Employees(
            Name=Name,
            Email=Email,
            Address=Address,
            Phone=Phone
        )
        emp.save()
        return redirect('home')
    
    return render(request,"base.html")

def edit(request):
    emp=Employees.objects.all()
    
    context={
        'emp':emp,
        
    }
    return redirect(request,'base.html',context)

def update(request,id):
    if request.method == "POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Address=request.POST.get('Address')
        Phone=request.POST.get('Phone')
        
        emp=Employees(
            id=id,
            Name=Name,
            Email=Email,
            Address=Address,
            Phone=Phone
        )
        emp.save()
        return redirect('home')
    
    
    return redirect(request,'base.html')


def delete(request,id):
    emp=Employees.objects.filter(id=id)
    emp.delete()
    
    return redirect("home")
    
    context={
        'emp':emp
        
    }
    
    
      