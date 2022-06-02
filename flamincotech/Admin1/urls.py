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
from Admin1 import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='adminshome'),
    path('deleteuser',views.deleteuser,name='deleteuser'),
    path('userlist/',views.userlist,name='userlist'),
    path('history/',views.history,name='history'),
    path('trackp/',views.trackp,name='trackp'),
    path('hardwaregeneral/',views.hardwaregeneral,name='hardwaregeneral'),
    path('hardwareipvariant/',views.hardwareipvariant,name='hardwareipvariant'),
    path('hardwareactive/',views.hardwareactive,name='hardwareactive'),
    path('hardwarepassive/',views.hardwarepassive,name='hardwarepassive'),
    path('hardwareethernet/',views.hardwareethernet,name='hardwareethernet'),
    path('hardwareddc/',views.hardwareddc,name='hardwareddc'),
    path('hardwarebmssensors/',views.hardwarebmssensors,name='hardwarebmssensors'),
    path('hardwarethirdparty/',views.hardwarethirdparty,name='hardwarethirdparty'),
    path('hardwarebmscabling/',views.hardwarebmscabling,name='hardwarebmscabling'),
    path('hardwarepiping/',views.hardwarepiping,name='hardwarepiping'),
    path('hardwaretrays/',views.hardwaretrays,name='hardwaretrays'),
    path('hardwaregeneralinstall/',views.hardwaregeneralinstall,name='hardwaregeneralinstall'),
    path('hardwareipvariantinstall/',views.hardwareipvariantinstall,name='hardwareipvariantinstall'),
    path('hardwareactiveinstall/',views.hardwareactiveinstall,name='hardwareactiveinstall'),
    path('hardwarepassiveinstall/',views.hardwarepassiveinstall,name='hardwarepassiveinstall'),
    path('hardwareethernetinstall/',views.hardwareethernetinstall,name='hardwareethernetinstall'),
    path('hardwareddcinstall/',views.hardwareddcinstall,name='hardwareddcinstall'),
    path('hardwarebmssensorsinstall/',views.hardwarebmssensorsinstall,name='hardwarebmssensorsinstall'),
    path('hardwarethirdpartyinstall/',views.hardwarethirdpartyinstall,name='hardwarethirdpartyinstall'),
    path('hardwarebmscablinginstall/',views.hardwarebmscablinginstall,name='hardwarebmscablinginstall'),
    path('hardwarepipinginstall/',views.hardwarepiping,name='hardwarepiping'),
    path('hardwaretraysinstall/',views.hardwaretrays,name='hardwaretrays'),
    path('edithardwaregeneral/',views.edithardwaregeneral,name='edithardwaregeneral'),
    path('edithardwareipvariant/',views.edithardwareipvariant,name='edithardwareipvariant'),
    path('edithardwareactive/',views.edithardwareactive,name='edithardwareactive'),
    path('edithardwarepassive/',views.edithardwarepassive,name='edithardwarepassive'),
    path('edithardwareethernet/',views.edithardwareethernet,name='edithardwareethernet'),
    path('edithardwareddc/',views.edithardwareddc,name='edithardwareddc'),
    path('edithardwarebmssensors/',views.edithardwarebmssensors,name='edithardwarebmssensors'),
    path('edithardwarethirdparty/',views.edithardwarethirdparty,name='edithardwarethirdparty'),
    path('edithardwarebmscabling/',views.edithardwarebmscabling,name='edithardwarebmscabling'),
    path('edithardwarepiping/',views.edithardwarepiping,name='edithardwarepiping'),
    path('edithardwaretrays/',views.edithardwaretrays,name='edithardwaretrays'),
    path('edithardwaregeneralinstall/',views.edithardwaregeneralinstall,name='edithardwaregeneralinstall'),
    path('edithardwareipvariantinstall/',views.edithardwareipvariantinstall,name='edithardwareipvariantinstall'),
    path('edithardwareactiveinstall/',views.edithardwareactiveinstall,name='edithardwareactiveinstall'),
    path('edithardwarepassiveinstall/',views.edithardwarepassiveinstall,name='edithardwarepassiveinstall'),
    path('edithardwareethernetinstall/',views.edithardwareethernetinstall,name='edithardwareethernetinstall'),
    path('edithardwareddcinstall/',views.edithardwareddcinstall,name='edithardwareddcinstall'),
    path('edithardwarebmssensorsinstall/',views.edithardwarebmssensorsinstall,name='edithardwarebmssensorsinstall'),
    path('edithardwarethirdpartyinstall/',views.edithardwarethirdpartyinstall,name='edithardwarethirdpartyinstall'),
    path('edithardwarebmscablinginstall/',views.edithardwarebmscablinginstall,name='edithardwarebmscablinginstall'),
    path('edithardwarepipinginstall/',views.edithardwarepiping,name='edithardwarepiping'),
    path('edithardwaretraysinstall/',views.edithardwaretrays,name='edithardwaretrays'),
    path('configuration/',views.configuration,name='configuration'),
    path('editconfiguration',views.editconfiguration,name='editconfiguration'),
    path('editconfiguration1',views.editconfiguration1,name='editconfiguration1'),
    path('vpss/',views.vpss1,name='vpss'),
    path('SpazioPriceCalculator/',views.SpazioPriceCalculators,name='SpazioPriceCalculator'),
    path('editvpss',views.editvpss,name='editvpss'),
    path('percentagechangesheet/',views.percentagechangesheet,name='percentagechangesheet'),
  
]