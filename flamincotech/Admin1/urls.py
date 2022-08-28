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
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from Admin1 import views
from django.views.static import serve
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='adminshome'),
    path('deleteuser',views.deleteuser,name='deleteuser'),
    path('history/',views.history,name='history'),
    path('trackp/',views.trackp,name='trackp'),
    path('hardwareactive/',views.hardwareactive,name='hardwareactive'),
    path('hardwaregeneral/',views.hardwaregeneral,name='hardwaregeneral'),
    path('hardwareipvariant/',views.hardwareipvariant,name='hardwareipvariant'),
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
    path('hardwarepipinginstall/',views.hardwarepipinginstall,name='hardwarepipinginstall'),
    path('hardwaretraysinstall/',views.hardwaretraysinstall,name='hardwaretraysinstall'),
    path('hardwaremaneffortsinstall/',views.hardwaremaneffortsinstall,name='hardwaremaneffortsinstall'),
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
    path('edithardwarepipinginstall/',views.edithardwarepipinginstall,name='edithardwarepipinginstall'),
    path('edithardwaretraysinstall/',views.edithardwaretraysinstall,name='edithardwaretraysinstall'),
    path('editmaneffortsinstall/',views.editmaneffortsinstall,name='editmaneffortsinstall'),
    path('configuration/',views.configuration,name='configuration'),
    path('editconfiguration',views.editconfiguration,name='editconfiguration'),
    path('editconfiguration1',views.editconfiguration1,name='editconfiguration1'),
    path('vpss/',views.vpss1,name='vpss1'),
    path('iandc/',views.iandc,name='iandc'),
    path('iandcedit/',views.iandcedit,name='iandcedit'),
    path('percentagechangesheet/',views.percentagechangesheet,name='percentagechangesheet'),
    path('export_vpss/',views.export_vpss1,name='export_vpss'),
    path('export_iandc/',views.export_iandc,name='export_iandc'),
    path('export_percentagechangesheet/',views.export_percentagechangesheet,name='export_percentagechangesheet'),
    path('vpssimport/',views.vpss1import,name='vpssimport'),
    
    
    path('import/',views.imports,name='import'),
    
    
    
    
    path('iandcimport/',views.iandcimport,name='iandcimport'),
    path('percentagechangesheetimport/',views.percentagechangesheetimport,name='percentagechangesheetimport'),
    path('SpazioPriceCalculator/',views.SpazioPriceCalculators,name='SpazioPriceCalculator'),
    path('SpazioPriceCalculatoredit/',views.SpazioPriceCalculatorsedit,name='SpazioPriceCalculatoredit'),
    path('userlist/',views.userlist,name='userlist'),
    path('export_SpazioPriceCalculator/',views.export_SpazioPriceCalculators,name='export_SpazioPriceCalculator'),
    path('export_userlist/',views.export_userlist,name='export_userlist'),
    path('editvpss',views.editvpss,name='editvpss'),
    path('automatepricing/',views.automatepricing,name='automatepricing'),
    path('export_automatepricing/',views.export_automatepricing,name='export_automatepricing'),
    path('automatepricingimport/',views.automatepricingimport,name='automatepricingimport'),
    path('SpazioPriceCalculator/editDBS/',views.editDBS,name='editDBS'),  
    path('SpazioPriceCalculator/editDUS/',views.editDUS,name='editDUS'),  
    path('SpazioPriceCalculator/editDPS/',views.editDPS,name='editDPS'),  
    path('SpazioPriceCalculator/editEOMA/',views.editEOMA,name='editEOMA'),  
    path('SpazioPriceCalculator/editRost/',views.editRost,name='editRost'),  
    path('detail_boq/',views.detail_boq,name='detail_boq'),  
    
    
    path('SpazioPriceCalculator/editWF/',views.editWF,name='editWF'),  
    path('SpazioPriceCalculator/editFB/',views.editFB,name='editFB'),  
    path('SpazioPriceCalculator/editKL/',views.editKL,name='editKL'),  
    path('SpazioPriceCalculator/editMRLO/',views.editMRLO,name='editMRLO'),  
    path('SpazioPriceCalculator/editMRLPC/',views.editMRLPC,name='editMRLPC'),  
    path('SpazioPriceCalculator/editMRLB/',views.editMRLB,name='editMRLB'),  
    
    
    path('SpazioPriceCalculator/editRLWFT/',views.editRLWFT,name='editRLWFT'),  
    path('SpazioPriceCalculator/editRLPC/',views.editRLPC,name='editRLPC'),  
    path('SpazioPriceCalculator/editRLO/',views.editRLO,name='editRLO'),  
    path('SpazioPriceCalculator/editHBTL/',views.editHBTL,name='editHBTL'),  
    path('editsoftwareextra',views.editsoftwareextra,name='editsoftwareextra'),  
    path('editautomate',views.editautomate,name='editautomate'),  
    path('hardwareactiveimport/',views.hardwareactiveimport,name='hardwareactiveimport'),
    path('hardwaregeneralimport/',views.hardwaregeneralimport,name='hardwaregeneralimport'),
    path('hardwareipvariantimport/',views.hardwareipvariantimport,name='hardwareipvariantimport'),
    path('hardwarepassiveimport/',views.hardwarepassiveimport,name='hardwarepassiveimport'),
    path('hardwareethernetimport/',views.hardwareethernetimport,name='hardwareethernetimport'),
    path('hardwareddcimport/',views.hardwareddcimport,name='hardwareddcimport'),
    path('hardwarebmssensorsimport/',views.hardwarebmssensorsimport,name='hardwarebmssensorsimport'),
    path('hardwarethirdpartyimport/',views.hardwarethirdpartyimport,name='hardwarethirdpartyimport'),
    path('hardwarebmscablingimport/',views.hardwarebmscablingimport,name='hardwarebmscablingimport'),
    path('hardwarepipingimport/',views.hardwarepipingimport,name='hardwarepipingimport'),
    path('hardwaretraysimport/',views.hardwaretraysimport,name='hardwaretraysimport'),
    path('hardwaregeneralinstallimport/',views.hardwaregeneralinstallimport,name='hardwaregeneralinstallimport'),
    path('hardwareipvariantinstallimport/',views.hardwareipvariantinstallimport,name='hardwareipvariantinstallimport'),
    path('hardwareactiveinstallimport/',views.hardwareactiveinstallimport,name='hardwareactiveinstallimport'),
    path('hardwarepassiveinstallimport/',views.hardwarepassiveinstallimport,name='hardwarepassiveinstallimport'),
    path('hardwareethernetinstallimport/',views.hardwareethernetinstallimport,name='hardwareethernetinstallimport'),
    path('hardwareddcinstallimport/',views.hardwareddcinstallimport,name='hardwareddcinstallimport'),
    path('hardwarebmssensorsinstallimport/',views.hardwarebmssensorsinstallimport,name='hardwarebmssensorsinstallimport'),
    path('hardwarethirdpartyinstallimport/',views.hardwarethirdpartyinstallimport,name='hardwarethirdpartyinstallimport'),
    path('hardwarebmscablinginstallimport/',views.hardwarebmscablinginstallimport,name='hardwarebmscablinginstallimport'),
    path('hardwarepipinginstallimport/',views.hardwarepipinginstallimport,name='hardwarepipinginstallimport'),
    path('hardwaretraysinstallimport/',views.hardwaretraysinstallimport,name='hardwaretraysinstallimport'),
    path('maneffortsinstallimport/',views.maneffortsinstallimport,name='maneffortsinstallimport'),
    
    
    
    path('export_hardwareactive/',views.export_hardwareactive,name='export_hardwareactive'),
    path('export_hardwaregeneral/',views.export_hardwaregeneral,name='export_hardwaregeneral'),
    path('export_hardwareipvariant/',views.export_hardwareipvariant,name='export_hardwareipvariant'),
    path('export_hardwarepassive/',views.export_hardwarepassive,name='export_hardwarepassive'),
    path('export_hardwareethernet/',views.export_hardwareethernet,name='export_hardwareethernet'),
    path('export_hardwareddc/',views.export_hardwareddc,name='export_hardwareddc'),
    path('export_hardwarebmssensors/',views.export_hardwarebmssensors,name='export_hardwarebmssensors'),
    path('export_hardwarethirdparty/',views.export_hardwarethirdparty,name='export_hardwarethirdparty'),
    path('export_hardwarebmscabling/',views.export_hardwarebmscabling,name='export_hardwarebmscabling'),
    path('export_hardwarepiping/',views.export_hardwarepiping,name='export_hardwarepiping'),
    path('export_hardwaretrays/',views.export_hardwaretrays,name='export_hardwaretrays'),
    path('export_hardwaregeneralinstall/',views.export_hardwaregeneralinstall,name='export_hardwaregeneralinstall'),
    path('export_hardwareipvariantinstall/',views.export_hardwareipvariantinstall,name='export_hardwareipvariantinstall'),
    path('export_hardwareactiveinstall/',views.export_hardwareactiveinstall,name='export_hardwareactiveinstall'),
    path('export_hardwarepassiveinstall/',views.export_hardwarepassiveinstall,name='export_hardwarepassiveinstall'),
    path('export_hardwareethernetinstall/',views.export_hardwareethernetinstall,name='export_hardwareethernetinstall'),
    path('export_hardwareddcinstall/',views.export_hardwareddcinstall,name='export_hardwareddcinstall'),
    path('export_hardwarebmssensorsinstall/',views.export_hardwarebmssensorsinstall,name='export_hardwarebmssensorsinstall'),
    path('export_hardwarethirdpartyinstall/',views.export_hardwarethirdpartyinstall,name='export_hardwarethirdpartyinstall'),
    path('export_hardwarebmscablinginstall/',views.export_hardwarebmscablinginstall,name='export_hardwarebmscablinginstall'),
    path('export_hardwarepipinginstall/',views.export_hardwarepipinginstall,name='export_hardwarepipinginstall'),
    path('export_hardwaretraysinstall/',views.export_hardwaretraysinstall,name='export_hardwaretraysinstall'),
    path('export_maneffortsinstall/',views.export_maneffortsinstall,name='export_maneffortsinstall'),
    
    
    path('db_general/',views.db_general,name='db_general'),
    path('detailed_boq/',views.detailed_boq,name='detailed_boq'),
    path('detailed_boqedit/',views.detailed_boqedit,name='detailed_boqedit'),
    path('margin/',views.margins,name='margin'),
    path('summary/',views.summarys,name='summary'),
    path('quotation/',views.quotations,name='quotation'),
    path('quotationedit/',views.quotationsedit,name='quotationedit'),
    path('adddata/',views.adddata,name='adddata'),
    re_path('^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('edit_quot_admin/<str:ref_no>', views.edit_quot_admin, name='edit_quot_admin')
    
    
]