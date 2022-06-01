from django.shortcuts import render
import json
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import InputConfiguration,vpss,HardWareGeneral,HardWareIpVariant,HardWareActive,HardWarePassive,HardWareEthernet,HardWareDdc,HardWareBmsSensors,HardWareThirdParty,HardWareBmsScabling,HardWarePiping,HardWareTrays,HardWareGeneralInstall,HardWareIpVariantInstall,HardWareActiveInstall,HardWarePassiveInstall,HardWareEthernetInstall,HardWareDdcInstall,HardWareBmsSensorsInstall,HardWareThirdPartyInstall,HardWareBmsScablingInstall,HardWarePipingInstall,HardWareTraysInstall,SpazioPriceCalculator,Desk_Booking_Solution,Desk_Utilization_Solution,Desk_Planning_Solution,Employee_One_Mobile_App,Rostering,Wayfinding,Feedback,Kiosk_License,Meeting_Room_License_Occupancy,Meeting_Room_License_People_Count,Meeting_Room_License_Booking,Restroom_License_People_Count,Restroom_License_Wet_floor_detection,Restroom_License_Odour ,Human_body_temperature_License
def index(request):
    return render(request,'Admin1/index.html')
def percentagechangesheet(request):
    entries=InputConfiguration.objects.all()
    print(len(entries))
    context={'entries':entries}
    return render(request,'Admin1/percentagechangesheet.html',context)

def registeruser(request):
    return render(request,'Admin1/registeruser.html')
def history(request):
    return render(request,'Admin1/history.html')
def trackp(request):
    return render(request,'Admin1/trackp.html')
def configuration(request):
    entries=InputConfiguration.objects.all()
    print(len(entries))
    context={'entries':entries}
    return render(request,'Admin1/configuration.html',context)
def editconfiguration(request):
    sr_no=request.POST.get('sr_no')
    sr_no1=sr_no
    sr_no=(int(sr_no))//10
    t=InputConfiguration.objects.get(sr_no=sr_no)
    t.active=request.POST.get('active')
    t.passive=request.POST.get('passive')
    t.ddcsensor=request.POST.get('ddcsensor')
    t.ft_hardware=request.POST.get('ft_hardware')
    t.cabpiptray=request.POST.get('cabpiptray')
    t.thirdparty=request.POST.get('thirdparty')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no1})
def editconfiguration1(request):
    sr_no=request.POST.get('sr_no')
    sr_no1=sr_no
    sr_no=(int(sr_no))//10
    t=InputConfiguration.objects.get(sr_no=sr_no)
    t.active1=request.POST.get('active')
    t.passive1=request.POST.get('passive')
    t.ddcsensor1=request.POST.get('ddcsensor')
    t.ft_hardware1=request.POST.get('ft_hardware')
    t.cabpiptray1=request.POST.get('cabpiptray')
    t.thirdparty1=request.POST.get('thirdparty')
    t.ftmandayeffort=request.POST.get('ftmandayeffort')
    t.othersmicffort=request.POST.get('othersmicffort')
    t.ft2=request.POST.get('ft2')
    t.ft3=request.POST.get('ft3')
    t.ft4=request.POST.get('ft4')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no1})
def vpss1(request):
    entries=vpss.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/vpss.html',context)
def editvpss(request):
    sr_no=request.POST.get('sr_no')
    t=vpss.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.TotalCost=request.POST.get('TotalCost')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.TotalPrice=request.POST.get('TotalPrice')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.FinalTotalPrice=request.POST.get('FinalTotalPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwaregeneral(request):
    entries=HardWareGeneral.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwaregeneral.html',context)
def edithardwaregeneral(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareGeneral.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareipvariant(request):
    entries=HardWareIpVariant.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareipvariant.html',context)
def edithardwareipvariant(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareIpVariant.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareactive(request):
    entries=HardWareActive.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareactive.html',context)
def edithardwareactive(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareActive.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarepassive(request):
    entries=HardWarePassive.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarepassive.html',context)
def edithardwarepassive(request):
    sr_no=request.POST.get('sr_no')
    t=HardWarePassive.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareethernet(request):
    entries=HardWareEthernet.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareethernet.html',context)
def edithardwareethernet(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareEthernet.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareddc(request):
    entries=HardWareDdc.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareddc.html',context)
def edithardwareddc(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareDdc.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarebmssensors(request):
    entries=HardWareBmsSensors.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarebmssensors.html',context)
def edithardwarebmssensors(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareBmsSensors.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarethirdparty(request):
    entries=HardWareThirdParty.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarethirdparty.html',context)
def edithardwarethirdparty(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareThirdParty.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarebmscabling(request):
    entries=HardWareBmsScabling.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarebmscabling.html',context)
def edithardwarebmscabling(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareBmsScabling.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarepiping(request):
    entries=HardWarePiping.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarepiping.html',context)
def edithardwarepiping(request):
    sr_no=request.POST.get('sr_no')
    t=HardWarePiping.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwaretrays(request):
    entries=HardWareTrays.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwaretrays.html',context)
def edithardwaretrays(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareTrays.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})

def hardwaregeneralinstall(request):
    entries=HardWareGeneralInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwaregeneralinstall.html',context)
def edithardwaregeneralinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareGeneralInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareipvariantinstall(request):
    entries=HardWareIpVariantInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareipvariantinstall.html',context)
def edithardwareipvariantinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareIpVariantInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareactiveinstall(request):
    entries=HardWareActiveInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareactiveinstall.html',context)
def edithardwareactiveinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareActiveInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarepassiveinstall(request):
    entries=HardWarePassiveInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarepassiveinstall.html',context)
def edithardwarepassiveinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWarePassiveInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareethernetinstall(request):
    entries=HardWareEthernetInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareethernetinstall.html',context)
def edithardwareethernetinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareEthernetInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwareddcinstall(request):
    entries=HardWareDdcInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwareddcinstall.html',context)

def SpazioPriceCalculators(request):
    entries=SpazioPriceCalculator.objects.all()
    InputConfigurations=InputConfiguration.objects.all()
    Desk_Booking_Solutions=Desk_Booking_Solution.objects.all()
    Desk_Utilization_Solutions=Desk_Utilization_Solution.objects.all()
    Desk_Planning_Solutions=Desk_Planning_Solution.objects.all()
    Employee_One_Mobile_Apps=Employee_One_Mobile_App.objects.all()
    Rosterings=Rostering.objects.all()
    Wayfindings=Wayfinding.objects.all()
    Feedbacks=Feedback.objects.all()
    Kiosk_Licenses=Kiosk_License.objects.all()
    Meeting_Room_License_Occupancys=Meeting_Room_License_Occupancy.objects.all()
    Meeting_Room_License_People_Counts=Meeting_Room_License_People_Count.objects.all()
    Meeting_Room_License_Bookings=Meeting_Room_License_Booking.objects.all()
    Restroom_License_People_Counts=Restroom_License_People_Count.objects.all()
    Restroom_License_Wet_floor_detections=Restroom_License_Wet_floor_detection.objects.all()
    Restroom_License_Odours =Restroom_License_Odour.objects.all()
    Human_body_temperature_Licenses=Human_body_temperature_License.objects.all()
    context={'entries':entries,'InputConfigurations':list(InputConfigurations.values()),'Desk_Booking_Solutions':list(Desk_Booking_Solutions.values()),'Desk_Utilization_Solutions':list(Desk_Utilization_Solutions.values()),'Desk_Planning_Solutions':list(Desk_Planning_Solutions.values()),'Employee_One_Mobile_Apps':list(Employee_One_Mobile_Apps.values()),'Rosterings':list(Rosterings.values()),'Wayfindings':list(Wayfindings.values()),'Feedbacks':list(Feedbacks.values()),'Kiosk_Licenses':list(Kiosk_Licenses.values()),'Meeting_Room_License_Occupancys':list(Meeting_Room_License_Occupancys.values()),'Meeting_Room_License_People_Counts':list(Meeting_Room_License_People_Counts.values()),'Meeting_Room_License_Bookings':list(Meeting_Room_License_Bookings.values()),'Restroom_License_People_Counts':list(Restroom_License_People_Counts.values()),'Restroom_License_Wet_floor_detections':list(Restroom_License_Wet_floor_detections.values()),'Restroom_License_Odours':list(Restroom_License_Odours.values()),'Human_body_temperature_Licenses':list(Human_body_temperature_Licenses.values())}
    
    return render(request,'Admin1/SpazioPriceCalculator.html',context)

def edithardwareddcinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareDdcInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarebmssensorsinstall(request):
    entries=HardWareBmsSensorsInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarebmssensorsinstall.html',context)
def edithardwarebmssensorsinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareBmsSensorsInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarethirdpartyinstall(request):
    entries=HardWareThirdPartyInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarethirdpartyinstall.html',context)
def edithardwarethirdpartyinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareThirdPartyInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarebmscablinginstall(request):
    entries=HardWareBmsScablingInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarebmscablinginstall.html',context)
def edithardwarebmscablinginstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareBmsScablingInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwarepipinginstall(request):
    entries=HardWarePipingInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwarepipinginstall.html',context)
def edithardwarepipinginstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWarePipingInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})
def hardwaretraysinstall(request):
    entries=HardWareTraysInstall.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/hardwaretraysinstall.html',context)
def edithardwaretraysinstall(request):
    sr_no=request.POST.get('sr_no')
    t=HardWareTraysInstall.objects.get(sr_no=sr_no)
    t.Qty=request.POST.get('Qty')
    t.InputPrice=request.POST.get('InputPrice')
    t.DiscountedPrice=request.POST.get('DiscountedPrice')
    t.InputCostInclusiveoffreight=request.POST.get('InputCostInclusiveoffreight')
    t.UnitCost=request.POST.get('UnitCost')
    t.UnitCostInclusiveofRisk=request.POST.get('UnitCostInclusiveofRisk')
    t.UnitCostInclusiveofContigency=request.POST.get('UnitCostInclusiveofContigency')
    t.Unit_Price=request.POST.get('Unit_Price')
    t.UnitPrice=request.POST.get('UnitPrice')
    t.ListPricewithoutRoundup=request.POST.get('ListPricewithoutRoundup')
    t.ListPricewithRoundedup=request.POST.get('ListPricewithRoundedup')
    t.save()
    return JsonResponse({'adg':'jyyj','sr_no':sr_no})


