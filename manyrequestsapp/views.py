from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def getinput(request):
    return render(request,'getinput.html')
def postinput(request):
    return render(request,'postinput.html')
def add(request):
    if request.method=="GET":
        p=int(request.GET["t1"])
        q=int(request.GET["t2"])
        r=p+q
        return HttpResponse("The sum is: "+str(r))
    else:
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        return HttpResponse("The sum is: "+str(z))
def sub(request):
    if request.method=="GET":
        a=int(request.GET["t3"])
        b=int(request.GET["t4"])
        c=a-b
        return HttpResponse("The sub is: "+str(c))
    else:
        e=int(request.GET["t3"])
        f=int(request.GET["t4"])
        g=e-f
        return HttpResponse("The sub is: "+str(g))
def mul(request):
    if request.method=="GET":
        h=int(request.GET["t5"])
        i=int(request.GET["t6"])
        j=h*i
        return HttpResponse("The mul is: "+str(j))
    else:
        m=int(request.GET["t5"])
        n=int(request.GET["t6"])
        o=m*n
        return HttpResponse("The mul is: "+str(o))
def div(request):
    if request.method=="GET":
        x=int(request.GET["t7"])
        y=int(request.GET["t8"])
        z=x/y
        return HttpResponse("The div is: "+str(z))
    else:
        t=int(request.GET["t9"])
        u=int(request.GET["t10"])
        l=t/u
        return HttpResponse("The div is: "+str(l))


