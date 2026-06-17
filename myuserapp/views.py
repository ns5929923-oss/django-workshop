from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return render(request, "home.html")

def Aboutpage(request):
    return render(request, "about.html")
    
def Contactpage(request):
    return render(request, "contact.html")

def Shoppage(request):
    return render(request, "shop.html")

def contactprocess(request):
    a= int(request.POST['txt1'])
    b= int(request.POST['txt2'])
    c= a + b
    msg= "A value is",a," " "B vlaue is",b, " " "sum is ",c
    return HttpResponse(msg)