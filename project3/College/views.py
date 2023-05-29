from django.shortcuts import render
from College.forms1 import CollForm
from College.models import Coll
# Create your views here.


#form1: builin form, with using objects

def details(request):
    objform =CollForm()
    if request.method == "POST":
        objform = CollForm(request.POST)  
        if objform.is_valid():
            objform.save()
            obj2 = Coll.objects.all()
            return render(request,'index.html',{'o2':obj2})
        else:
            objform = CollForm()
    return render(request,'form1.html',{'f1':objform})

def viewdetail(request):
    obj2 = Coll.objects.all()
    return render(request,'index.html',{'o2':obj2})

def home(request):
    return render(request,'home.html')



#form2: userdefined without using objects

def list(request):
    allobj = Coll.objects.all()
    return render(request,'index.html',{'o2':allobj})

def details2(request):
    formobj = CollForm()
    if request.method== "POST":
        formobj = CollForm(request.POST)
        
        if formobj.is_valid():
            formobj.save()
            return list(request)
        else:
            formobj = CollForm()
    return render(request,'form2.html')

#form3: userdefined using objects

def list(request):
    allobj = Coll.objects.all()
    return render(request,'index.html',{'o2':allobj})

def details3(request):

    if request.method== "POST":
        nm= request.POST['n']
        pl= request.POST['p']
        pi= request.POST['pin']

        obj = Coll.objects.create(name=nm,place=pl,pincode=pi)
        obj.save
        
        return list(request)
        
    return render(request,'form3.html')