"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from User import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='userhome'),
    path('createquotation/',views.createquotation,name='createquotation'),
    path('history/',views.history,name='history'),
    path('quotation/',views.quotations,name='quotation'),
    path('quotationedit/',views.quotationsedit,name='quotationedit'),
    path('detailed_boq/',views.detailed_boq,name='detailed_boq'),
    path('detailed_boqedit/<str:ref_no>',views.detailed_boqedit,name='detailed_boqedit'),
    path('SpazioPriceCalculator/',views.SpazioPriceCalculators,name='SpazioPriceCalculator'),
    path('SpazioPriceCalculatoredit/',views.SpazioPriceCalculatorsedit,name='SpazioPriceCalculatoredit'),
    path('iandc/',views.iandc,name='iandc'),
    path('iandcedit/',views.iandcedit,name='iandcedit'),
    path('edit_quot_user/<str:ref_no>', views.edit_quot_user, name='edit_quot_user')
]