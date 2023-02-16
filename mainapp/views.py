from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
def home(request):
    data= Employee.objects.all()
    return render(request,"index.html",{"Data":data})

def addRecord(request):
    if(request.method=='POST'):
        e = Employee()
        e.name = request.POST.get("name")
        e.email=request.POST.get("email")
        e.phone=request.POST.get("phone")
        e.salary=request.POST.get("salary")
        e.dsg = request.POST.get("dsg")
        e.city = request.POST.get("city")
        e.state = request.POST.get("state")
        e.save()
        return HttpResponseRedirect("/")
    return render(request,"add.html")   

    
def editRecord(request,Id):
    data = Employee.objects.get(Id=Id)
    if(request.method=='POST'):
        data.name = request.POST.get("name")
        data.email=request.POST.get("email")
        data.phone=request.POST.get("phone")
        data.salary=request.POST.get("salary")
        data.dsg = request.POST.get("dsg")
        data.city = request.POST.get("city")
        data.state = request.POST.get("state")
        data.save()
        return HttpResponseRedirect("/")
    return render(request,"update.html",{"Data":data})    
def deleteRecord(request,Id):
    data=Employee.objects.filter(Id=Id)
    data.delete()
    return HttpResponseRedirect("/")
    
# Create your views here.
