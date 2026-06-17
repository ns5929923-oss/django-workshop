from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage),
    path('Homepage',views.Homepage),
    path('Aboutpage',views.Aboutpage),
    path('Contactpage',views.Contactpage),
    path('Shoppage',views.Shoppage),
    path('contactprocess', views.contactprocess)

]
