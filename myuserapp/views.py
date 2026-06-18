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
    c= int(request.POST['txt3'])
    d= int(request.POST['txt4'])
    e= int(request.POST['txt5'])
    f= a+b+c+d+e
    g=(f/500)*100

    msg= "Subject1 marks",a,"Subject2 marks",b, "Subject3 marks",c, "Subject4 marks",d, "Subject5",e,"Sum of marks",f, "Percentage",g

    result=""
    if g>90:
        result="Your garde A+"
    elif (g>80 and g<90):
        result="Your garde A"
    elif(g>60 and g<50):
        result="Your garde is B"
    elif(g>50 and g<30):
        result="Your grade is C"
    else:
        result= "You failed!"

    return render(request, 'result.html',{'mya':a, 'myb':b, 'myc': c, 'myd':d, 'mye':e, 'myf':f, 'myg':g, 'result':result})