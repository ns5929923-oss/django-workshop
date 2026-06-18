from django.shortcuts import render,redirect
from django.http import HttpResponse

def Homepage(request):
    return render(request, "home.html")

def Aboutpage(request):
    return render(request, "about.html")
    
def Contactpage(request):
    return render(request, "contact.html")

def Shoppage(request):
    return render(request, "shop.html")

def createsession(request):
    request.session['username']= "Cherry"
    return HttpResponse("session created")

def getsession(request):
    if request.session.has_key('username'):
        msg = request.session['username']
        return HttpResponse(msg)
    else:
        return HttpResponse("session is not present")
    
def deletesession(request):
    del request.session['username']
    return HttpResponse("session removed")


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

def loginpage(request):
    return render(request, 'login.html')

def loginprocess(request):
    txt= request.POST['email']
    request.session['myemail']=txt
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request, "dashboard.html")
    else:
        return redirect(loginpage)
    
def logout(request):
    del request.session['myemail']
    return redirect(loginpage)

