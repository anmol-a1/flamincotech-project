from django.shortcuts import render,redirect
import json
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from Admin1.models import Quotation,Soft_Items_DB,margin,ManEffortsInstall,IandC,NewUser,Software_Revised_Extra,Automate_Pricing,InputConfiguration,vpss,HardWareGeneral,HardWareIpVariant,HardWareActive,HardWarePassive,HardWareEthernet,HardWareDdc,HardWareBmsSensors,HardWareThirdParty,HardWareBmsScabling,HardWarePiping,HardWareTrays,HardWareGeneralInstall,HardWareIpVariantInstall,HardWareActiveInstall,HardWarePassiveInstall,HardWareEthernetInstall,HardWareDdcInstall,HardWareBmsSensorsInstall,HardWareThirdPartyInstall,HardWareBmsScablingInstall,HardWarePipingInstall,HardWareTraysInstall,SpazioPriceCalculator,Desk_Booking_Solution,Desk_Utilization_Solution,Desk_Planning_Solution,Employee_One_Mobile_App,Rostering,Wayfinding,Feedback,Kiosk_License,Meeting_Room_License_Occupancy,Meeting_Room_License_People_Count,Meeting_Room_License_Booking,Restroom_License_People_Count,Restroom_License_Wet_floor_detection,Restroom_License_Odour ,Human_body_temperature_License
from .models import Soft_Items,Bms_Trays,Bms_Piping,Bms_Cabling,Bms_Sensors,Ddc,Ethernet,Fiber,Active,General,Others,Third_Party
import datetime
from import_export import resources
from django.shortcuts import get_object_or_404
import tablib
from tablib import Dataset
import mimetypes
# import os module
from json import dumps
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes
def index(request):
	return render(request,'User/index.html')
def createquotation(request):
	return render(request,'User/clientdetails.html')
def history(request):
	objs=Quotation.objects.filter(user_name=request.user.user_name)
	context={'entries':objs}
	return render(request,'User/history.html',context)
def SpazioPriceCalculators(request):
	entries=SpazioPriceCalculator.objects.all()
	Software_Revised_Extras=Software_Revised_Extra.objects.all()
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
	Automate_Pricings=Automate_Pricing.objects.all()
	context={'entries':entries,'Software_Revised_Extras':list(Software_Revised_Extras.values()),'InputConfigurations':list(InputConfigurations.values()),'Automate_Pricings':list(Automate_Pricings.values()),'Desk_Booking_Solutions':list(Desk_Booking_Solutions.values()),'Desk_Utilization_Solutions':list(Desk_Utilization_Solutions.values()),'Desk_Planning_Solutions':list(Desk_Planning_Solutions.values()),'Employee_One_Mobile_Apps':list(Employee_One_Mobile_Apps.values()),'Rosterings':list(Rosterings.values()),'Wayfindings':list(Wayfindings.values()),'Feedbacks':list(Feedbacks.values()),'Kiosk_Licenses':list(Kiosk_Licenses.values()),'Meeting_Room_License_Occupancys':list(Meeting_Room_License_Occupancys.values()),'Meeting_Room_License_People_Counts':list(Meeting_Room_License_People_Counts.values()),'Meeting_Room_License_Bookings':list(Meeting_Room_License_Bookings.values()),'Restroom_License_People_Counts':list(Restroom_License_People_Counts.values()),'Restroom_License_Wet_floor_detections':list(Restroom_License_Wet_floor_detections.values()),'Restroom_License_Odours':list(Restroom_License_Odours.values()),'Human_body_temperature_Licenses':list(Human_body_temperature_Licenses.values())}
	
	return render(request,'User/SpazioPriceCalculator.html',context)
def SpazioPriceCalculatorsedit(request):
	entries=SpazioPriceCalculator.objects.all()
	Software_Revised_Extras=Software_Revised_Extra.objects.all()
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
	Automate_Pricings=Automate_Pricing.objects.all()
	context={'entries':entries,'Software_Revised_Extras':list(Software_Revised_Extras.values()),'InputConfigurations':list(InputConfigurations.values()),'Automate_Pricings':list(Automate_Pricings.values()),'Desk_Booking_Solutions':list(Desk_Booking_Solutions.values()),'Desk_Utilization_Solutions':list(Desk_Utilization_Solutions.values()),'Desk_Planning_Solutions':list(Desk_Planning_Solutions.values()),'Employee_One_Mobile_Apps':list(Employee_One_Mobile_Apps.values()),'Rosterings':list(Rosterings.values()),'Wayfindings':list(Wayfindings.values()),'Feedbacks':list(Feedbacks.values()),'Kiosk_Licenses':list(Kiosk_Licenses.values()),'Meeting_Room_License_Occupancys':list(Meeting_Room_License_Occupancys.values()),'Meeting_Room_License_People_Counts':list(Meeting_Room_License_People_Counts.values()),'Meeting_Room_License_Bookings':list(Meeting_Room_License_Bookings.values()),'Restroom_License_People_Counts':list(Restroom_License_People_Counts.values()),'Restroom_License_Wet_floor_detections':list(Restroom_License_Wet_floor_detections.values()),'Restroom_License_Odours':list(Restroom_License_Odours.values()),'Human_body_temperature_Licenses':list(Human_body_temperature_Licenses.values())}
	
	return render(request,'User/SpazioPriceCalculatoredit.html',context)

def iandc(request):
	entries=IandC.objects.all()
	hardeffortman1 = ManEffortsInstall.objects.get(sr_no=1)
	hardeffortman2 = ManEffortsInstall.objects.get(sr_no=3)
	hardeffortman3 = ManEffortsInstall.objects.get(sr_no=4)
	hardeffortman4 = ManEffortsInstall.objects.get(sr_no=5)
	context={'entries':entries,'hardeffortman1':hardeffortman1,'hardeffortman2':hardeffortman2,'hardeffortman3':hardeffortman3,'hardeffortman4':hardeffortman4}
	return render(request,'User/iandc.html',context)
def iandcedit(request):
	entries=IandC.objects.all()
	hardeffortman1 = ManEffortsInstall.objects.get(sr_no=1)
	hardeffortman2 = ManEffortsInstall.objects.get(sr_no=3)
	hardeffortman3 = ManEffortsInstall.objects.get(sr_no=4)
	hardeffortman4 = ManEffortsInstall.objects.get(sr_no=5)
	context={'entries':entries,'hardeffortman1':hardeffortman1,'hardeffortman2':hardeffortman2,'hardeffortman3':hardeffortman3,'hardeffortman4':hardeffortman4}
	return render(request,'User/iandcedit.html',context)
def detailed_boq(request):
	Ddc1=Ddc.objects.all()
	Bms_Trays1=Bms_Trays.objects.all()
	Bms_Piping1=Bms_Piping.objects.all()
	Bms_Cabling1=Bms_Cabling.objects.all()
	Bms_Sensor1=Bms_Sensors.objects.all()
	Ethernet1=Ethernet.objects.all()
	Fiber1=Fiber.objects.all()
	Active1=Active.objects.all()
	General1=General.objects.all()
	Others1=Others.objects.all()
	abcd=General.objects.all()
	Third_Party1=Third_Party.objects.all()
	HardWareGenerals=HardWareGeneral.objects.all()
	HardWareIpVariants=HardWareIpVariant.objects.all()
	HardWareGeneralInstalls=HardWareGeneralInstall.objects.all()
	HardWareActives=HardWareActive.objects.all()
	HardWareActivesInstall=HardWareActiveInstall.objects.all()
	HardWarePassives=HardWarePassive.objects.all()
	HardWarePassivesInstall=HardWarePassiveInstall.objects.all()
	HardWareEthernets=HardWareEthernet.objects.all()
	HardWareEthernetsInstall=HardWareEthernetInstall.objects.all()
	HardWareDdcs=HardWareDdc.objects.all()
	HardWareDdcsInstall=HardWareDdcInstall.objects.all()
	HardWarePipings=HardWarePiping.objects.all()
	HardWarePipingsInstall=HardWarePipingInstall.objects.all()
	HardWareBmsSensorss=HardWareBmsSensors.objects.all()
	HardWareBmsSensorssInstall=HardWareBmsSensorsInstall.objects.all()
	HardWareBmsScablings=HardWareBmsScabling.objects.all()
	HardWareBmsScablingsInstall=HardWareBmsScablingInstall.objects.all()
	HardWareThirdPartys=HardWareThirdParty.objects.all()
	HardWareThirdPartysInstall=HardWareThirdPartyInstall.objects.all()
	HardWareTrayss=HardWareTrays.objects.all()
	HardWareTrayssInstall=HardWareTraysInstall.objects.all()
	ManEffortsInstalls=ManEffortsInstall.objects.all()
	vpsss=vpss.objects.all()
	entries1=vpsss[0:7]
	entries2=vpsss[7:]
	soft_items=Soft_Items_DB.objects.all()
#  HardWareTrays,HardWareTraysInstall
	context={'soft_data':list(soft_items.values()),'hard_data':list(abcd.values()),'Software_Items':soft_items,'ManEfforts': ManEffortsInstalls,'ManEffortsData':list(ManEffortsInstalls.values()),'vpssdata':list(vpsss.values()),'Trays1':entries1,'Trays2':entries2,'TraysDatas':list(HardWareTrayss.values()),'TraysDatasInstall': list(HardWareTrayssInstall.values()),'PipingDatas':list(HardWarePipings.values()),'PipingDatasInstall': list(HardWarePipingsInstall.values()),'BmsScablingDatas':list(HardWareBmsScablings.values()),'BmsScablingDatasInstall': list(HardWareBmsScablingsInstall.values()),'ThirdPartyDatas':list(HardWareThirdPartys.values()),'ThirdPartyDatasInstall': list(HardWareThirdPartysInstall.values()),'BmsSensorsDatas':list(HardWareBmsSensorss.values()),'BmsSensorsDatasInstall': list(HardWareBmsSensorssInstall.values()),'DdcDatas':list(HardWareDdcs.values()),'DdcDatasInstall': list(HardWareDdcsInstall.values()),'EthernetDatas':list(HardWareEthernets.values()),'EthernetDatasInstall': list(HardWareEthernetsInstall.values()),'PassiveDatas':list(HardWarePassives.values()),'PassiveDatasInstall': list(HardWarePassivesInstall.values()),'HardWareActives':list(HardWareActives.values()),'HardWareActivesInstall':list(HardWareActivesInstall.values()),'HardWareGeneralInstalls':list(HardWareGeneralInstalls.values()),'HardGeneral':list(HardWareGenerals.values()),'HardIP':list(HardWareIpVariants.values()),'Ddc':HardWareDdcs,'Bms_Trays':HardWareTrayss,'Bms_Piping':HardWarePipings,'Bms_Cabling':HardWareBmsScablings,'Bms_Sensor':HardWareBmsSensorss,'Ethernet':HardWareEthernets,'Fiber':HardWarePassives,'Active':HardWareActives,'General':abcd,'Others':Others1,'Third_Party':HardWareThirdPartys}
	
	return render(request,'User/detailed_boq/main.html',context)
def detailed_boqedit(request,ref_no):
	Ddc1=Ddc.objects.all()
	Bms_Trays1=Bms_Trays.objects.all()
	Bms_Piping1=Bms_Piping.objects.all()
	Bms_Cabling1=Bms_Cabling.objects.all()
	Bms_Sensor1=Bms_Sensors.objects.all()
	Ethernet1=Ethernet.objects.all()
	Fiber1=Fiber.objects.all()
	Active1=Active.objects.all()
	General1=General.objects.all()
	Others1=Others.objects.all()
	abcd=General.objects.all()
	Third_Party1=Third_Party.objects.all()
	HardWareGenerals=HardWareGeneral.objects.all()
	HardWareIpVariants=HardWareIpVariant.objects.all()
	HardWareGeneralInstalls=HardWareGeneralInstall.objects.all()
	HardWareActives=HardWareActive.objects.all()
	HardWareActivesInstall=HardWareActiveInstall.objects.all()
	HardWarePassives=HardWarePassive.objects.all()
	HardWarePassivesInstall=HardWarePassiveInstall.objects.all()
	HardWareEthernets=HardWareEthernet.objects.all()
	HardWareEthernetsInstall=HardWareEthernetInstall.objects.all()
	HardWareDdcs=HardWareDdc.objects.all()
	HardWareDdcsInstall=HardWareDdcInstall.objects.all()
	HardWarePipings=HardWarePiping.objects.all()
	HardWarePipingsInstall=HardWarePipingInstall.objects.all()
	HardWareBmsSensorss=HardWareBmsSensors.objects.all()
	HardWareBmsSensorssInstall=HardWareBmsSensorsInstall.objects.all()
	HardWareBmsScablings=HardWareBmsScabling.objects.all()
	HardWareBmsScablingsInstall=HardWareBmsScablingInstall.objects.all()
	HardWareThirdPartys=HardWareThirdParty.objects.all()
	HardWareThirdPartysInstall=HardWareThirdPartyInstall.objects.all()
	HardWareTrayss=HardWareTrays.objects.all()
	HardWareTrayssInstall=HardWareTraysInstall.objects.all()
	ManEffortsInstalls=ManEffortsInstall.objects.all()
	vpsss=vpss.objects.all()
	entries1=vpsss[0:7]
	entries2=vpsss[7:]
	soft_items=Soft_Items_DB.objects.all()
	obj=Quotation.objects.get(ref_no=ref_no)
	print(str(obj.input_data))
	print(obj.input_data)
	dataDictionary = {

		'bms_trays':obj._Bms_Trays,
		'bms_piping':obj._Bms_Piping,
		'bms_cabling':obj._Bms_Cabling,
		'bms_sensor':obj._Bms_Sensors,
		'ddc':obj._Ddc,
		'ethernet':obj._Ethernet,
		'fiber':obj._Fiber,
		'active':obj._Active,
		'efforts':obj._Efforts,
		'others':obj._Others,
		'third_party':obj._Third_Party,
		'trays2':obj._Trays2
		
	}
	dataJSON = dumps(dataDictionary)
#  HardWareTrays,HardWareTraysInstall
	context={'data':dataJSON,'soft_data':list(soft_items.values()),'hard_data':list(abcd.values()),'Software_Items':soft_items,'ManEfforts': ManEffortsInstalls,'ManEffortsData':list(ManEffortsInstalls.values()),'vpssdata':list(vpsss.values()),'Trays1':entries1,'Trays2':entries2,'TraysDatas':list(HardWareTrayss.values()),'TraysDatasInstall': list(HardWareTrayssInstall.values()),'PipingDatas':list(HardWarePipings.values()),'PipingDatasInstall': list(HardWarePipingsInstall.values()),'BmsScablingDatas':list(HardWareBmsScablings.values()),'BmsScablingDatasInstall': list(HardWareBmsScablingsInstall.values()),'ThirdPartyDatas':list(HardWareThirdPartys.values()),'ThirdPartyDatasInstall': list(HardWareThirdPartysInstall.values()),'BmsSensorsDatas':list(HardWareBmsSensorss.values()),'BmsSensorsDatasInstall': list(HardWareBmsSensorssInstall.values()),'DdcDatas':list(HardWareDdcs.values()),'DdcDatasInstall': list(HardWareDdcsInstall.values()),'EthernetDatas':list(HardWareEthernets.values()),'EthernetDatasInstall': list(HardWareEthernetsInstall.values()),'PassiveDatas':list(HardWarePassives.values()),'PassiveDatasInstall': list(HardWarePassivesInstall.values()),'HardWareActives':list(HardWareActives.values()),'HardWareActivesInstall':list(HardWareActivesInstall.values()),'HardWareGeneralInstalls':list(HardWareGeneralInstalls.values()),'HardGeneral':list(HardWareGenerals.values()),'HardIP':list(HardWareIpVariants.values()),'Ddc':HardWareDdcs,'Bms_Trays':HardWareTrayss,'Bms_Piping':HardWarePipings,'Bms_Cabling':HardWareBmsScablings,'Bms_Sensor':HardWareBmsSensorss,'Ethernet':HardWareEthernets,'Fiber':HardWarePassives,'Active':HardWareActives,'General':abcd,'Others':Others1,'Third_Party':HardWareThirdPartys}
	
	return render(request,'User/detailed_boq/mainedit.html',context)
def quotations(request):
	return render(request,'User/pdf.html')
def quotationsedit(request):
	return render(request,'User/pdfedit.html')

def edit_quot_user(request,ref_no):
	obj=Quotation.objects.get(ref_no=ref_no)
	print(str(obj.input_data))
	print(obj.input_data)
	dataDictionary = {
		'ref_no':obj.ref_no,
		'company_name':obj.company_name,
		'input_data':obj.input_data,
		'user_name':obj.user_name
	}
	dataJSON = dumps(dataDictionary)
	return render(request, 'User/clientdetailsedit.html', {'data': dataJSON})