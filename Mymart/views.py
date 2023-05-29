from django.shortcuts import render

def home(request):
    return render(request,"Mymart/index.html ")
def register(request):
    return render(request,"Mymart/register.html ")

