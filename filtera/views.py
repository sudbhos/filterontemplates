from django.shortcuts import render
from .models import Demoinfo
# Create your views here.
def testview(request):
    my_data=Demoinfo.objects.all()
    return render(request,"testapp/test.html",{'my_data':my_data})

def lowerview(request):
    my_data = Demoinfo.objects.all()
    return render(request,"testapp/lower.html",{'my_data':my_data})

def upperi(request):
    my_data = Demoinfo.objects.all()
    return render(request,"testapp/upper.html",{'my_data':my_data})