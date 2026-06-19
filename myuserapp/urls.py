from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage),
    path('Homepage',views.Homepage),
    path('Aboutpage',views.Aboutpage),
    path('Contactpage',views.Contactpage),
    path('Shoppage',views.Shoppage),
    path('contactprocess', views.contactprocess),
    
    path('setsession', views.createsession),
    path('getsession', views.getsession),
    path('deletesession', views.deletesession),
    
    path('loginpage', views.loginpage),
    path('loginprocess', views.loginprocess),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    
    path('maildemo', views.maildemo),
    path('process', views.mailsendprocess, name='process'),
    path('contactus', views.contactpageview, name='contactus'),
    path('counts', views.count),

    path('studentform', views.studentform),
    path('studentformprocess',views.studentformprocess),
    path('display_student', views.display_student),
    path('delete_student/<int:id>/', views.delete_student)

]
