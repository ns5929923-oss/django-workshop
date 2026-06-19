from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . models import student

def Homepage(request):
    return render(request, "home.html")

def Aboutpage(request):
    return render(request, "about.html")
    
def Contactpage(request):
    return render(request, "contact.html")

def Shoppage(request):
    return render(request, "shop.html")

# Marksheet

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

# Session management

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

# Session & login

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

# Static mail sending process

def maildemo(request):
    subject = 'Django masil demo'
    message = 'code sucessfully run'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nehasinghtomar239@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Mail Sent")
 
 # Dynamic mail sending process
def mailsendprocess(request):
    subject = request.POST['txt7']
    message = request.POST['txt8']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.POST['txt6'],]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Mail Sent")
    
def contactpageview(request):
    return render(request, 'contactus.html')


# Page refresh counter

def count(request):
    if request.session.has_key('count'):
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    return HttpResponse(f"Page refreshed {request.session['count']} times")



# Database
def studentform(request):
    return render(request, 'signup.html')

def studentformprocess(request):
    txt1=request.POST['txt1']
    txt2=request.POST['txt2']
    txt3=request.POST['txt3']
    txt4=request.POST['txt4']
    txt5=request.POST['txt5']
    student.objects.create(Name=txt1, Email=txt2, Mobile=txt3,Age=txt4, Address=txt5)
    return HttpResponse("Thankyou~~")

  #  subject = 'Signed Up'
    message = 'Successfully Signed Up'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.POST['txt2'],]
    send_mail(subject, message, email_from, recipient_list)
   

    subject = 'Alert'
    message = 'Someone signed up'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nehasinghtomar239@gmail.com']
    send_mail(subject, message, email_from, recipient_list)

def display_student(request):
    studentlist= student.objects.all()
    return render (request, 'display-student.html', {'student': studentlist}) 

def delete_student(request, id):
    student.objects.get(id=id).delete()
    return redirect('display_student')
       
   
