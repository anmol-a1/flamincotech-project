from django.shortcuts import render,redirect
import json
from django.db.models import Count
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import Pm_Final,Pm_After_Margin,Pm_After_Cost,Quotation,Soft_Items_DB,margin,ManEffortsInstall,IandC,NewUser,Software_Revised_Extra,Automate_Pricing,InputConfiguration,vpss,HardWareGeneral,HardWareIpVariant,HardWareActive,HardWarePassive,HardWareEthernet,HardWareDdc,HardWareBmsSensors,HardWareThirdParty,HardWareBmsScabling,HardWarePiping,HardWareTrays,HardWareGeneralInstall,HardWareIpVariantInstall,HardWareActiveInstall,HardWarePassiveInstall,HardWareEthernetInstall,HardWareDdcInstall,HardWareBmsSensorsInstall,HardWareThirdPartyInstall,HardWareBmsScablingInstall,HardWarePipingInstall,HardWareTraysInstall,SpazioPriceCalculator,Desk_Booking_Solution,Desk_Utilization_Solution,Desk_Planning_Solution,Employee_One_Mobile_App,Rostering,Wayfinding,Feedback,Kiosk_License,Meeting_Room_License_Occupancy,Meeting_Room_License_People_Count,Meeting_Room_License_Booking,Restroom_License_People_Count,Restroom_License_Wet_floor_detection,Restroom_License_Odour ,Human_body_temperature_License
from User.models import Soft_Items,Bms_Trays,Bms_Piping,Bms_Cabling,Bms_Sensors,Ddc,Ethernet,Fiber,Active,General,Others,Third_Party
import datetime
from import_export import resources
from django.shortcuts import get_object_or_404
import tablib
from tablib import Dataset
import mimetypes
import math
# import os module
from json import dumps
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes
#     company_name=models.CharField(max_length=100)

#Bms_Trays,Bms_Piping,Bms_Cabling,Bms_Sensors,Ddc,Ethernet,Fiber,Active,General,Others,Third_Party
def adddata(request):
	print(request.POST.get('action'))
	if request.POST.get('action') == 'post':
		try:
			created=Quotation.objects.update_or_create(ref_no=request.POST.get('ref_no'),pdf=request.FILES.get('pdf'),company_name=request.POST.get('company_name'),input_data=request.POST.get('input_data'),excel=request.FILES.get('excel'),user_name=request.user.user_name,emp_name=request.user.first_name,_Bms_Trays=request.POST.get('Bms_Trays'),_Bms_Piping=request.POST.get('Bms_Piping'),_Bms_Cabling=request.POST.get('Bms_Cabling'),_Bms_Sensors=request.POST.get('Bms_Sensors'),_Ddc=request.POST.get('Ddc'),_Ethernet=request.POST.get('Ethernet'),_Fiber=request.POST.get('Fiber'),_Active=request.POST.get('Active'),_Efforts=request.POST.get('Efforts'),_Others=request.POST.get('Others'),_Third_Party=request.POST.get('Third_Party'),_Trays2=request.POST.get('Trays2'),description=request.POST.get('description'),_hard=request.POST.get('_hard'))
		except:
			try:
				member = Quotation.objects.get(ref_no=request.POST.get('ref_no'))
				member.pdf=request.FILES.get('pdf')
				member.company_name=request.POST.get('company_name')
				member.excel =request.FILES.get('excel')
				member.input_data=request.POST.get('input_data')
				member._Bms_Trays=request.POST.get('Bms_Trays')
				member._Bms_Piping=request.POST.get('Bms_Piping')
				member._Bms_Cabling=request.POST.get('Bms_Cabling')
				member._Bms_Sensors=request.POST.get('Bms_Sensors')
				member._Ddc=request.POST.get('Ddc')
				member._Ethernet=request.POST.get('Ethernet')
				member._Fiber=request.POST.get('Fiber')
				member._Trays2=request.POST.get('Trays2')
				member._Active=request.POST.get('Active')
				member._Efforts=request.POST.get('Efforts')
				member._Others=request.POST.get('Others')
				member._hard=request.POST.get('_hard')
				member._Third_Party=request.POST.get('Third_Party')
				member.description=request.POST.get('description')
				#member.user_email=request.user.email
				member.save()
			except:
				print("mahaerror")
	return JsonResponse({'result':'', })
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
	Pm_Finals=Pm_Final.objects.all()
	Pm_After_Margins=Pm_After_Margin.objects.all()
	Pm_After_Costs=Pm_After_Cost.objects.all()
	vpsss=vpss.objects.all()
	entries1=vpsss[0:7]
	entries2=vpsss[7:]
	soft_items=Soft_Items_DB.objects.all()
#  HardWareTrays,HardWareTraysInstall
	context={'generaldata':list(General1.values()),'Pm_Finals':list(Pm_Finals.values()),'Pm_After_Margins':list(Pm_After_Margins.values()),'Pm_After_Costs':list(Pm_After_Costs.values()),'soft_data':list(soft_items.values()),'hard_data':list(abcd.values()),'Software_Items':soft_items,'ManEfforts': ManEffortsInstalls,'ManEffortsData':list(ManEffortsInstalls.values()),'vpssdata':list(vpsss.values()),'Trays1':entries1,'Trays2':entries2,'TraysDatas':list(HardWareTrayss.values()),'TraysDatasInstall': list(HardWareTrayssInstall.values()),'PipingDatas':list(HardWarePipings.values()),'PipingDatasInstall': list(HardWarePipingsInstall.values()),'BmsScablingDatas':list(HardWareBmsScablings.values()),'BmsScablingDatasInstall': list(HardWareBmsScablingsInstall.values()),'ThirdPartyDatas':list(HardWareThirdPartys.values()),'ThirdPartyDatasInstall': list(HardWareThirdPartysInstall.values()),'BmsSensorsDatas':list(HardWareBmsSensorss.values()),'BmsSensorsDatasInstall': list(HardWareBmsSensorssInstall.values()),'DdcDatas':list(HardWareDdcs.values()),'DdcDatasInstall': list(HardWareDdcsInstall.values()),'EthernetDatas':list(HardWareEthernets.values()),'EthernetDatasInstall': list(HardWareEthernetsInstall.values()),'PassiveDatas':list(HardWarePassives.values()),'PassiveDatasInstall': list(HardWarePassivesInstall.values()),'HardWareActives':list(HardWareActives.values()),'HardWareActivesInstall':list(HardWareActivesInstall.values()),'HardWareGeneralInstalls':list(HardWareGeneralInstalls.values()),'HardGeneral':list(HardWareGenerals.values()),'HardIP':list(HardWareIpVariants.values()),'Ddc':HardWareDdcs,'Bms_Trays':HardWareTrayss,'Bms_Piping':HardWarePipings,'Bms_Cabling':HardWareBmsScablings,'Bms_Sensor':HardWareBmsSensorss,'Ethernet':HardWareEthernets,'Fiber':HardWarePassives,'Active':HardWareActives,'General':abcd,'Others':Others1,'Third_Party':HardWareThirdPartys}
	
	return render(request,'Admin1/main.html',context)
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
	Pm_Finals=Pm_Final.objects.all()
	Pm_After_Margins=Pm_After_Margin.objects.all()
	Pm_After_Costs=Pm_After_Cost.objects.all()
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
		'hards':obj._hard,
		'third_party':obj._Third_Party,
		'trays2':obj._Trays2
		
	}
	dataJSON = dumps(dataDictionary)
#  HardWareTrays,HardWareTraysInstall
	context={'generaldata':list(General1.values()),'Pm_Finals':list(Pm_Finals.values()),'Pm_After_Margins':list(Pm_After_Margins.values()),'Pm_After_Costs':list(Pm_After_Costs.values()),'data':dataJSON,'soft_data':list(soft_items.values()),'hard_data':list(abcd.values()),'Software_Items':soft_items,'ManEfforts': ManEffortsInstalls,'ManEffortsData':list(ManEffortsInstalls.values()),'vpssdata':list(vpsss.values()),'Trays1':entries1,'Trays2':entries2,'TraysDatas':list(HardWareTrayss.values()),'TraysDatasInstall': list(HardWareTrayssInstall.values()),'PipingDatas':list(HardWarePipings.values()),'PipingDatasInstall': list(HardWarePipingsInstall.values()),'BmsScablingDatas':list(HardWareBmsScablings.values()),'BmsScablingDatasInstall': list(HardWareBmsScablingsInstall.values()),'ThirdPartyDatas':list(HardWareThirdPartys.values()),'ThirdPartyDatasInstall': list(HardWareThirdPartysInstall.values()),'BmsSensorsDatas':list(HardWareBmsSensorss.values()),'BmsSensorsDatasInstall': list(HardWareBmsSensorssInstall.values()),'DdcDatas':list(HardWareDdcs.values()),'DdcDatasInstall': list(HardWareDdcsInstall.values()),'EthernetDatas':list(HardWareEthernets.values()),'EthernetDatasInstall': list(HardWareEthernetsInstall.values()),'PassiveDatas':list(HardWarePassives.values()),'PassiveDatasInstall': list(HardWarePassivesInstall.values()),'HardWareActives':list(HardWareActives.values()),'HardWareActivesInstall':list(HardWareActivesInstall.values()),'HardWareGeneralInstalls':list(HardWareGeneralInstalls.values()),'HardGeneral':list(HardWareGenerals.values()),'HardIP':list(HardWareIpVariants.values()),'Ddc':HardWareDdcs,'Bms_Trays':HardWareTrayss,'Bms_Piping':HardWarePipings,'Bms_Cabling':HardWareBmsScablings,'Bms_Sensor':HardWareBmsSensorss,'Ethernet':HardWareEthernets,'Fiber':HardWarePassives,'Active':HardWareActives,'General':abcd,'Others':Others1,'Third_Party':HardWareThirdPartys}
	
	return render(request,'Admin1/mainedit.html',context)
def fetchdata():
	context={}
	InputConfigurations=InputConfiguration.objects.all()
	for i in range(len(InputConfigurations)):
		context[f"InputConfigurations{i+1}"]=InputConfigurations[i]
	return context
def iandc(request):
	entries=IandC.objects.all()
	hardeffortman1 = ManEffortsInstall.objects.get(sr_no=1)
	hardeffortman2 = ManEffortsInstall.objects.get(sr_no=3)
	hardeffortman3 = ManEffortsInstall.objects.get(sr_no=4)
	hardeffortman4 = ManEffortsInstall.objects.get(sr_no=5)
	context={'entries':entries,'hardeffortman1':hardeffortman1,'hardeffortman2':hardeffortman2,'hardeffortman3':hardeffortman3,'hardeffortman4':hardeffortman4}
	return render(request,'Admin1/iandc.html',context)
def iandcedit(request):
	entries=IandC.objects.all()
	hardeffortman1 = ManEffortsInstall.objects.get(sr_no=1)
	hardeffortman2 = ManEffortsInstall.objects.get(sr_no=3)
	hardeffortman3 = ManEffortsInstall.objects.get(sr_no=4)
	hardeffortman4 = ManEffortsInstall.objects.get(sr_no=5)
	context={'entries':entries,'hardeffortman1':hardeffortman1,'hardeffortman2':hardeffortman2,'hardeffortman3':hardeffortman3,'hardeffortman4':hardeffortman4}
	return render(request,'Admin1/iandcedit.html',context)
class IandCResource(resources.ModelResource):
	class Meta:
		model = IandC
def export_iandc(request):
	member_resource =IandCResource()
	dataset = member_resource.export()
	fname=f"member-data {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def iandcimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
		except:
			return redirect('iandc')
		try:
			for data in imported_data:	
				print(data)
				IandC.objects.create(sr_no=int(data[0]),Deployment_Activity=data[1],Resource_Level=data[2],Common=int(data[3]),Spazio_Software=int(data[4]),Meeting_Room_Booking=int(data[5]),Meeting_Room_People_count_occupancy=int(data[6]),Restroom_Hygiene=int(data[7]),IAQ_Automate=int(data[8]),Wayfinding=int(data[9]),Feedback=int(data[10]))

		except:
			print("errored")
			pass    
		return redirect('iandc')
def index(request):
	return render(request,'Admin1/index.html')
def summarys(request):
	return render(request,'Admin1/summary.html')
def quotations(request):
	return render(request,'Admin1/pdf.html')
def quotationsedit(request):
	return render(request,'Admin1/pdfedit.html')
def margins(request):
	context={'Margin':margin.objects.all()}
	return render(request,'Admin1/margin.html',context)
def deleteuser(request):
	if request.POST.get('action') == 'post':
		NewUser.objects.filter(user_name=request.POST.get('user_name')).delete()
		return JsonResponse({'user_name':request.POST.get('user_name'),'error':'None' })
	return JsonResponse({'error':'error', })
def userlist(request):
	context={'users':NewUser.objects.all()}
	return render(request,'Admin1/userlist.html',context)
class NewUserResource(resources.ModelResource):
	class Meta:
		model = NewUser
def export_userlist(request):
	member_resource =NewUserResource()
	dataset = member_resource.export()
	fname=f"User List {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def history(request):
	objs=Quotation.objects.filter(user_name=request.user.user_name)
	print(request.user.user_name)
	print(objs)
	context={'entries':objs}
	return render(request,'Admin1/history.html',context)
def historycheck(request,user_name):
	objs=Quotation.objects.filter(user_name=user_name)
	context={'entries':objs}
	return render(request,'Admin1/history.html',context)
def download_pdf(request, filename=''):
	if filename != '':
		filename=f"{filename}.pdf"
		filepath = 'media/pdfs/' + filename
		path = open(filepath, 'rb')
		mime_type, _ = mimetypes.guess_type(filepath)
		response = HttpResponse(path, content_type=mime_type)
		response['Content-Disposition'] = "attachment; filename=%s" % filename
		# Return the response value
		return response
	else:
		print("error")
def download(request, path):
	# get the download path
	download_path = os.path.join(settings.MEDIA_ROOT, path)
	if os.path.exists(download_path):
		with open(download_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/adminupload")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
			return response
	raise Http404
	
	
		
# class HardWareGeneralResource(resources.ModelResource):
# 	class Meta:
# 		model = HardWareGeneral
# def export_hardwaregeneral(request):
# 	member_resource =HardWareGeneralResource()
# 	dataset = member_resource.export()
# 	fname=f"member-data {datetime.datetime.now().date()}"
# 	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
# 	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
# 	return response
def trackp(request):
	result = (Quotation.objects.values('user_name','emp_name').annotate(dcount=Count('user_name')).order_by())
	context={'entries':result}
	return render(request,'Admin1/trackp.html',context)
# class HardWareGeneralResource(resources.ModelResource):
# 	class Meta:
# 		model = HardWareGeneral
# def export_hardwaregeneral(request):
# 	member_resource =HardWareGeneralResource()
# 	dataset = member_resource.export()
# 	fname=f"member-data {datetime.datetime.now().date()}"
# 	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
# 	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
# 	return response

def configuration(request):
	entries=InputConfiguration.objects.all()
	print(len(entries))
	context={'entries':entries}
	return render(request,'Admin1/configuration.html',context)
def detail_boq(request):
	Generals=General.objects.all()
	Soft_Itemss=Soft_Items.objects.all()
	Bms_Trayss=Bms_Trays.objects.all()
	Bms_Pipings=Bms_Piping.objects.all()
	Bms_Cablings=Bms_Cabling.objects.all()
	Bms_Sensorss=Bms_Sensors.objects.all()
	Ddcs=Ddc.objects.all()
	Ethernets=Ethernet.objects.all()
	Fibers=Fiber.objects.all()
	Actives=Active.objects.all()
	HardwareGenerals=HardWareGeneral.objects.all()
	context={'General':Generals,'Soft_Items':Soft_Itemss,'Bms_Trays':Bms_Trayss,'Bms_Piping':Bms_Pipings,'Bms_Cabling':Bms_Cablings,'Bms_Sensors':Bms_Sensorss,'Ddc':Ddcs,'Ethernet':Ethernets,'Fiber':Fibers,'Active':Actives,'HardwareGeneral':list(HardwareGenerals.values())}
	return render(request,'Admin1/detailed_boq.html',context)
class InputConfigurationResource(resources.ModelResource):
	class Meta:
		model = InputConfiguration
def export_configuration(request):
	member_resource =InputConfigurationResource()
	dataset = member_resource.export()
	fname=f"member-data {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def configurationimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			InputConfiguration.objects.all().delete()
		except:
			return redirect('configuration')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				InputConfiguration.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('configuration')
def vpss1(request):
	entries=vpss.objects.all()
	entries1=entries[0:7]
	entries2=entries[7:]
	context=fetchdata()
	context['entries1']=entries1
	context['entries2']=entries2
	return render(request,'Admin1/vpss.html',context)
class vpssResource(resources.ModelResource):
	class Meta:
		model = vpss
def export_vpss1(request):
	member_resource =vpssResource()
	dataset = member_resource.export()
	fname=f"Variable Project Specific Sheet {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def vpss1import(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			vpss.objects.all().delete()
		except:
			return redirect('vpss1')
		try:
			for data in imported_data:
				print(data)
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				vpss.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),TotalCost=int(data[17]),Margin=int(data[18]),Unit_Price=int(data[19]),TotalPrice=int(data[20]),WarrantyCharges=int(data[21]),UnitPrice=int(data[22]),FinalTotalPrice=int(data[23]),InsuranceCharges=int(data[24]),ListPricewithoutRoundup=int(data[25]),ListPricewithRoundedup=int(data[26]))
		except:
			print("errored")
			pass    
		return redirect('vpss1')



#########




def db_general(request):
	entries=General.objects.all()
	context={'entries':entries}
	return render(request,'User/detailed_boq/hardware_items.html',context)

##########

def imports(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			Bms_Cabling.objects.all().delete()
		except:
			return redirect('db_general')
		try:
			for data in imported_data:
				print(data)	
				Bms_Cabling.objects.create(sr_no=int(data[0]),Make=data[1],Model=data[2],Hardware_Items=data[3],Qty=int(data[4]),Uom=data[5],Cost_Supply_Rate=int(data[6]),Cost_Supply_Total=int(data[7]),Cost_Installation_Rate=int(data[8]),Cost_Installation_Total=int(data[9]),MRS_Rate=int(data[10]),MRS_Total=int(data[11]),MRI_Rate=int(data[12]),MRI_Total=int(data[13]),Supply_Rate=int(data[14]),Supply_Total=int(data[15]),Installation_Rate=int(data[16]),Installation_Total=int(data[17]))
		except:
			print("errored")
			pass    
		return redirect('db_general')
#Soft_Items

#     Installation_Rate
#     Installation_Total
#     Remarks=models.CharFi
#     Minimum_Qty
#     Minimum_Installation


#     Make
#     Model
#     Hardware_Items
#     Qty
#     Uom
#     Cost_Supply_Rate
#     Cost_Supply_Total
#     Cost_Installation_Rate
#     Cost_Installation_Total
#     MRS_Rate
#     MRS_Total
#     MRI_Rate
#     MRI_Total
#     Supply_Rate
#     Supply_Total







#################

def percentagechangesheet(request):
	entries=InputConfiguration.objects.all()
	print(len(entries))
	context={'entries':entries}
	return render(request,'Admin1/percentagechangesheet.html',context)
class InputConfigurationResource(resources.ModelResource):
	class Meta:
		model = InputConfiguration
def export_percentagechangesheet(request):
	member_resource =InputConfigurationResource()
	dataset = member_resource.export()
	fname=f"Percentage Change Sheet {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def percentagechangesheetimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			InputConfiguration.objects.all().delete()
		except:
			return redirect('percentagechangesheet')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				InputConfiguration.objects.create(sr_no=int(data[0]),desc=data[1],ft_hardware=float(data[2]),active=float(data[3]),passive=float(data[4]),ddcsensor=float(data[5]),thirdparty=float(data[6]),cabpiptray=float(data[7]),ft_hardware1=float(data[8]),active1=float(data[9]),passive1=float(data[10]),ddcsensor1=float(data[11]),thirdparty1=float(data[12]),cabpiptray1=float(data[13]),ftmandayeffort=float(data[14]),othersmicffort=float(data[15]),ft2=float(data[16]),ft3=float(data[17]),ft4=float(data[18]))
		except:
			print("errored")
			pass    
		return redirect('percentagechangesheet')
def editsoftwareextra(request):
	sr_no=request.POST.get('sr_no')
	t=Software_Revised_Extra.objects.get(sr_no=sr_no)
	t.Key=request.POST.get('Key')
	t.Value=request.POST.get('Value')
	t.Info=request.POST.get('Info')
	t.save()
	return JsonResponse({'adg':'jyyj',})
def editconfiguration1(request):
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
 #ftmandayeffort,othersmicffort,ft2,ft3,ft4
	t.ftmandayeffort=request.POST.get('ftmandayeffort')
	t.othersmicffort=request.POST.get('othersmicffort')
	t.ft2=request.POST.get('ft2')
	t.ft3=request.POST.get('ft3')
	t.tft4=request.POST.get('ft4')

	t.save()
	temp=InputConfiguration.objects.all()
#,,,,,,,,,,
	generalobjs=HardWareGeneralInstall.objects.all()
	bmscabobjs=HardWareBmsScablingInstall.objects.all()
	pipobjs=HardWarePipingInstall.objects.all()
	traysobjs=HardWareTraysInstall.objects.all()
	activeobjs=HardWareActiveInstall.objects.all()
	passiveobjs=HardWarePassiveInstall.objects.all()
	ddcobjs=HardWareDdcInstall.objects.all()
	etherobjs=HardWareEthernetInstall.objects.all()
	thirdpartyobjs=HardWareThirdPartyInstall.objects.all()
	bmssensorobjs=HardWareBmsSensorsInstall.objects.all()
	maneffortobjs=ManEffortsInstall.objects.all()
	vpsss=vpss.objects.all()
	othersobjs=vpsss[0:7]
	trays1objs=vpsss[7:18]
	generalobjs1=generalobjs[0:1]
	generalobjs2=generalobjs[1:6]
	generalobjs3=generalobjs[6:10]
	generalobjs4=generalobjs[10:]
	for obj in generalobjs1:
		obj.Discount=temp[0].ft_hardware1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ft_hardware1)/100))
		obj.Freight=temp[1].ft_hardware1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ft_hardware1)/100))
		obj.InterestCOM=temp[2].ft_hardware1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ft_hardware1)/100))
		obj.InwardTax=temp[3].ft_hardware1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ft_hardware1)/100))
		obj.ContigencyPercentage=temp[4].ft_hardware1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ft_hardware1)/100))
		obj.Margin=temp[5].ft_hardware1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ft_hardware1)))
		obj.WarrantyCharges=temp[6].ft_hardware1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ft_hardware1)/100))
		obj.InsuranceCharges=temp[7].ft_hardware1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ft_hardware1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/500)*500)
		obj.save()
	for obj in generalobjs2:
		obj.Discount=temp[0].ft_hardware1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ft_hardware1)/100))
		obj.Freight=temp[1].ft_hardware1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ft_hardware1)/100))
		obj.InterestCOM=temp[2].ft_hardware1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ft_hardware1)/100))
		obj.InwardTax=temp[3].ft_hardware1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ft_hardware1)/100))
		obj.ContigencyPercentage=temp[4].ft_hardware1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ft_hardware1)/100))
		obj.Margin=temp[5].ft_hardware1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ft_hardware1)))
		obj.WarrantyCharges=temp[6].ft_hardware1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ft_hardware1)/100))
		obj.InsuranceCharges=temp[7].ft_hardware1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ft_hardware1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in generalobjs3:
		obj.Discount=temp[0].ft_hardware1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ft_hardware1)/100))
		obj.Freight=temp[1].ft_hardware1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ft_hardware1)/100))
		obj.InterestCOM=temp[2].ft_hardware1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ft_hardware1)/100))
		obj.InwardTax=temp[3].ft_hardware1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ft_hardware1)/100))
		obj.ContigencyPercentage=temp[4].ft_hardware1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ft_hardware1)/100))
		obj.Margin=temp[5].ft_hardware1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ft_hardware1)))
		obj.WarrantyCharges=temp[6].ft_hardware1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ft_hardware1)/100))
		obj.InsuranceCharges=temp[7].ft_hardware1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ft_hardware1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/500)*500)
	for obj in generalobjs4:
		obj.Discount=temp[0].ft_hardware1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ft_hardware1)/100))
		obj.Freight=temp[1].ft_hardware1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ft_hardware1)/100))
		obj.InterestCOM=temp[2].ft_hardware1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ft_hardware1)/100))
		obj.InwardTax=temp[3].ft_hardware1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ft_hardware1)/100))
		obj.ContigencyPercentage=temp[4].ft_hardware1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ft_hardware1)/100))
		obj.Margin=temp[5].ft_hardware1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ft_hardware1)))
		obj.WarrantyCharges=temp[6].ft_hardware1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ft_hardware1)/100))
		obj.InsuranceCharges=temp[7].ft_hardware1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ft_hardware1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/100)*100)
		obj.save()
	
	for obj in activeobjs:
		obj.Discount=temp[0].active1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].active1)/100))
		obj.Freight=temp[1].active1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].active1)/100))
		obj.InterestCOM=temp[2].active1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].active1)/100))
		obj.InwardTax=temp[3].active1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].active1)/100))
		obj.ContigencyPercentage=temp[4].active1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].active1)/100))
		obj.Margin=temp[5].active1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].active1)))
		obj.WarrantyCharges=temp[6].active1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].active1)/100))
		obj.InsuranceCharges=temp[7].active1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].active1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()


	for obj in passiveobjs:
		obj.Discount=temp[0].passive1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].passive1)/100))
		obj.Freight=temp[1].passive1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].passive1)/100))
		obj.InterestCOM=temp[2].passive1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].passive1)/100))
		obj.InwardTax=temp[3].passive1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].passive1)/100))
		obj.ContigencyPercentage=temp[4].passive1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].passive1)/100))
		obj.Margin=temp[5].passive1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].passive1)))
		obj.WarrantyCharges=temp[6].passive1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].passive1)/100))
		obj.InsuranceCharges=temp[7].passive1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].passive1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()


	for obj in etherobjs:
		obj.Discount=temp[0].passive1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].passive1)/100))
		obj.Freight=temp[1].passive1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].passive1)/100))
		obj.InterestCOM=temp[2].passive1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].passive1)/100))
		obj.InwardTax=temp[3].passive1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].passive1)/100))
		obj.ContigencyPercentage=temp[4].passive1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].passive1)/100))
		obj.Margin=temp[5].passive1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].passive1)))
		obj.WarrantyCharges=temp[6].passive1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].passive1)/100))
		obj.InsuranceCharges=temp[7].passive1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].passive1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()


	for obj in ddcobjs:
		obj.Discount=temp[0].ddcsensor1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ddcsensor1)/100))
		obj.Freight=temp[1].ddcsensor1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ddcsensor1)/100))
		obj.InterestCOM=temp[2].ddcsensor1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ddcsensor1)/100))
		obj.InwardTax=temp[3].ddcsensor1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ddcsensor1)/100))
		obj.ContigencyPercentage=temp[4].ddcsensor1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ddcsensor1)/100))
		obj.Margin=temp[5].ddcsensor1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ddcsensor1)))
		obj.WarrantyCharges=temp[6].ddcsensor1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ddcsensor1)/100))
		obj.InsuranceCharges=temp[7].ddcsensor1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ddcsensor1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in bmssensorobjs:
		obj.Discount=temp[0].ddcsensor1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ddcsensor1)/100))
		obj.Freight=temp[1].ddcsensor1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ddcsensor1)/100))
		obj.InterestCOM=temp[2].ddcsensor1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ddcsensor1)/100))
		obj.InwardTax=temp[3].ddcsensor1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ddcsensor1)/100))
		obj.ContigencyPercentage=temp[4].ddcsensor1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ddcsensor1)/100))
		obj.Margin=temp[5].ddcsensor1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ddcsensor1)))
		obj.WarrantyCharges=temp[6].ddcsensor1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ddcsensor1)/100))
		obj.InsuranceCharges=temp[7].ddcsensor1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ddcsensor1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()


	for obj in thirdpartyobjs:
		obj.Discount=temp[0].thirdparty1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].thirdparty1)/100))
		obj.Freight=temp[1].thirdparty1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].thirdparty1)/100))
		obj.InterestCOM=temp[2].thirdparty1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].thirdparty1)/100))
		obj.InwardTax=temp[3].thirdparty1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].thirdparty1)/100))
		obj.ContigencyPercentage=temp[4].thirdparty1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].thirdparty1)/100))
		obj.Margin=temp[5].thirdparty1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].thirdparty1)))
		obj.WarrantyCharges=temp[6].thirdparty1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].thirdparty1)/100))
		obj.InsuranceCharges=temp[7].thirdparty1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].thirdparty1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()


#bmscabobjs,pipobjs,traysobjs

	for obj in bmscabobjs:
		obj.Discount=temp[0].cabpiptray1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].cabpiptray1)/100))
		obj.Freight=temp[1].cabpiptray1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].cabpiptray1)/100))
		obj.InterestCOM=temp[2].cabpiptray1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].cabpiptray1)/100))
		obj.InwardTax=temp[3].cabpiptray1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].cabpiptray1)/100))
		obj.ContigencyPercentage=temp[4].cabpiptray1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].cabpiptray1)/100))
		obj.Margin=temp[5].cabpiptray1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].cabpiptray1)))
		obj.WarrantyCharges=temp[6].cabpiptray1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].cabpiptray1)/100))
		obj.InsuranceCharges=temp[7].cabpiptray1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].cabpiptray1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()


	for obj in pipobjs:
		obj.Discount=temp[0].cabpiptray1
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].cabpiptray1)/100))
		obj.Freight=temp[1].cabpiptray1
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].cabpiptray1)/100))
		obj.InterestCOM=temp[2].cabpiptray1
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].cabpiptray1)/100))
		obj.InwardTax=temp[3].cabpiptray1
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].cabpiptray1)/100))
		obj.ContigencyPercentage=temp[4].cabpiptray1
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].cabpiptray1)/100))
		obj.Margin=temp[5].cabpiptray1
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].cabpiptray1)))
		obj.WarrantyCharges=temp[6].cabpiptray1
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].cabpiptray1)/100))
		obj.InsuranceCharges=temp[7].cabpiptray1
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].cabpiptray1/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()


	for obj in traysobjs:
		obj.Discount=temp[0].cabpiptray
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].cabpiptray)/100))
		obj.Freight=temp[1].cabpiptray
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].cabpiptray)/100))
		obj.InterestCOM=temp[2].cabpiptray
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].cabpiptray)/100))
		obj.InwardTax=temp[3].cabpiptray
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].cabpiptray)/100))
		obj.ContigencyPercentage=temp[4].cabpiptray
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].cabpiptray)/100))
		obj.Margin=temp[5].cabpiptray
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].cabpiptray)))
		obj.WarrantyCharges=temp[6].cabpiptray
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].cabpiptray)/100))
		obj.InsuranceCharges=temp[7].cabpiptray
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].cabpiptray/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in maneffortobjs:
		obj.Discount=temp[0].ftmandayeffort
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ftmandayeffort)/100))
		obj.Freight=temp[1].ftmandayeffort
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ftmandayeffort)/100))
		obj.InterestCOM=temp[2].ftmandayeffort
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ftmandayeffort)/100))
		obj.InwardTax=temp[3].ftmandayeffort
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ftmandayeffort)/100))
		obj.ContigencyPercentage=temp[4].ftmandayeffort
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ftmandayeffort)/100))
		obj.Margin=temp[5].ftmandayeffort
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ftmandayeffort)))
		obj.WarrantyCharges=temp[6].ftmandayeffort
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ftmandayeffort)/100))
		obj.InsuranceCharges=temp[7].ftmandayeffort
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ftmandayeffort/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in trays1objs:
		obj.Discount=temp[0].ddcsensor
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ddcsensor)/100))
		obj.Freight=temp[1].ddcsensor
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ddcsensor)/100))
		obj.InterestCOM=temp[2].ddcsensor
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ddcsensor)/100))
		obj.InwardTax=temp[3].ddcsensor
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ddcsensor)/100))
		obj.ContigencyPercentage=temp[4].ddcsensor
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ddcsensor)/100))
		obj.Margin=temp[5].ddcsensor
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ddcsensor)))
		obj.WarrantyCharges=temp[6].ddcsensor
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ddcsensor)/100))
		obj.InsuranceCharges=temp[7].ddcsensor
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ddcsensor/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in othersobjs:
		obj.Discount=temp[0].othersmicffort
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].othersmicffort)/100))
		obj.Freight=temp[1].othersmicffort
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].othersmicffort)/100))
		obj.InterestCOM=temp[2].othersmicffort
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].othersmicffort)/100))
		obj.InwardTax=temp[3].othersmicffort
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].othersmicffort)/100))
		obj.ContigencyPercentage=temp[4].othersmicffort
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].othersmicffort)/100))
		obj.Margin=temp[5].othersmicffort
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].othersmicffort)))
		obj.WarrantyCharges=temp[6].othersmicffort
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].othersmicffort)/100))
		obj.InsuranceCharges=temp[7].othersmicffort
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].othersmicffort/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()

##







	
	return JsonResponse({'adg':'jyyj','sr_no':sr_no1})
def editconfiguration(request):
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
	temp=InputConfiguration.objects.all()
	
	generalobjs=HardWareGeneral.objects.all()
	ipobjs=HardWareIpVariant.objects.all()

	bmscabobjs=HardWareBmsScabling.objects.all()
	pipobjs=HardWarePiping.objects.all()
	traysobjs=HardWareTrays.objects.all()
	activeobjs=HardWareActive.objects.all()
	passiveobjs=HardWarePassive.objects.all()
	ddcobjs=HardWareDdc.objects.all()
	etherobjs=HardWareEthernet.objects.all()
	thirdpartyobjs=HardWareThirdParty.objects.all()
	bmssensorobjs=HardWareBmsSensors.objects.all()
	for obj in generalobjs:
		obj.Discount=temp[0].ft_hardware
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ft_hardware)/100))
		obj.Freight=temp[1].ft_hardware
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ft_hardware)/100))
		obj.InterestCOM=temp[2].ft_hardware
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ft_hardware)/100))
		obj.InwardTax=temp[3].ft_hardware
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ft_hardware)/100))
		obj.ContigencyPercentage=temp[4].ft_hardware
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ft_hardware)/100))
		obj.Margin=temp[5].ft_hardware
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ft_hardware)))
		obj.WarrantyCharges=temp[6].ft_hardware
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ft_hardware)/100))
		obj.InsuranceCharges=temp[7].ft_hardware
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ft_hardware/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in ipobjs:
		obj.Discount=temp[0].ft_hardware
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ft_hardware)/100))
		obj.Freight=temp[1].ft_hardware
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ft_hardware)/100))
		obj.InterestCOM=temp[2].ft_hardware
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ft_hardware)/100))
		obj.InwardTax=temp[3].ft_hardware
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ft_hardware)/100))
		obj.ContigencyPercentage=temp[4].ft_hardware
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ft_hardware)/100))
		obj.Margin=temp[5].ft_hardware
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ft_hardware)))
		obj.WarrantyCharges=temp[6].ft_hardware
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ft_hardware)/100))
		obj.InsuranceCharges=temp[7].ft_hardware
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ft_hardware/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in activeobjs:
		obj.Discount=temp[0].active
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].active)/100))
		obj.Freight=temp[1].active
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].active)/100))
		obj.InterestCOM=temp[2].active
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].active)/100))
		obj.InwardTax=temp[3].active
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].active)/100))
		obj.ContigencyPercentage=temp[4].active
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].active)/100))
		obj.Margin=temp[5].active
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].active)))
		obj.WarrantyCharges=temp[6].active
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].active)/100))
		obj.InsuranceCharges=temp[7].active
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].active/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in passiveobjs:
		obj.Discount=temp[0].passive
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].passive)/100))
		obj.Freight=temp[1].passive
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].passive)/100))
		obj.InterestCOM=temp[2].passive
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].passive)/100))
		obj.InwardTax=temp[3].passive
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].passive)/100))
		obj.ContigencyPercentage=temp[4].passive
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].passive)/100))
		obj.Margin=temp[5].passive
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].passive)))
		obj.WarrantyCharges=temp[6].passive
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].passive)/100))
		obj.InsuranceCharges=temp[7].passive
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].passive/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in etherobjs:
		obj.Discount=temp[0].passive
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].passive)/100))
		obj.Freight=temp[1].passive
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].passive)/100))
		obj.InterestCOM=temp[2].passive
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].passive)/100))
		obj.InwardTax=temp[3].passive
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].passive)/100))
		obj.ContigencyPercentage=temp[4].passive
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].passive)/100))
		obj.Margin=temp[5].passive
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].passive)))
		obj.WarrantyCharges=temp[6].passive
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].passive)/100))
		obj.InsuranceCharges=temp[7].passive
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].passive/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in ddcobjs:
		obj.Discount=temp[0].ddcsensor
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ddcsensor)/100))
		obj.Freight=temp[1].ddcsensor
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ddcsensor)/100))
		obj.InterestCOM=temp[2].ddcsensor
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ddcsensor)/100))
		obj.InwardTax=temp[3].ddcsensor
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ddcsensor)/100))
		obj.ContigencyPercentage=temp[4].ddcsensor
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ddcsensor)/100))
		obj.Margin=temp[5].ddcsensor
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ddcsensor)))
		obj.WarrantyCharges=temp[6].ddcsensor
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ddcsensor)/100))
		obj.InsuranceCharges=temp[7].ddcsensor
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ddcsensor/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in bmssensorobjs:
		obj.Discount=temp[0].ddcsensor
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].ddcsensor)/100))
		obj.Freight=temp[1].ddcsensor
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].ddcsensor)/100))
		obj.InterestCOM=temp[2].ddcsensor
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].ddcsensor)/100))
		obj.InwardTax=temp[3].ddcsensor
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].ddcsensor)/100))
		obj.ContigencyPercentage=temp[4].ddcsensor
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].ddcsensor)/100))
		obj.Margin=temp[5].ddcsensor
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].ddcsensor)))
		obj.WarrantyCharges=temp[6].ddcsensor
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].ddcsensor)/100))
		obj.InsuranceCharges=temp[7].ddcsensor
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].ddcsensor/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in thirdpartyobjs:
		obj.Discount=temp[0].thirdparty
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].thirdparty)/100))
		obj.Freight=temp[1].thirdparty
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].thirdparty)/100))
		obj.InterestCOM=temp[2].thirdparty
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].thirdparty)/100))
		obj.InwardTax=temp[3].thirdparty
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].thirdparty)/100))
		obj.ContigencyPercentage=temp[4].thirdparty
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].thirdparty)/100))
		obj.Margin=temp[5].thirdparty
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].thirdparty)))
		obj.WarrantyCharges=temp[6].thirdparty
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].thirdparty)/100))
		obj.InsuranceCharges=temp[7].thirdparty
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].thirdparty/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
#bmscabobjs,pipobjs,traysobjs

	for obj in bmscabobjs:
		obj.Discount=temp[0].cabpiptray
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].cabpiptray)/100))
		obj.Freight=temp[1].cabpiptray
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].cabpiptray)/100))
		obj.InterestCOM=temp[2].cabpiptray
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].cabpiptray)/100))
		obj.InwardTax=temp[3].cabpiptray
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].cabpiptray)/100))
		obj.ContigencyPercentage=temp[4].cabpiptray
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].cabpiptray)/100))
		obj.Margin=temp[5].cabpiptray
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].cabpiptray)))
		obj.WarrantyCharges=temp[6].cabpiptray
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].cabpiptray)/100))
		obj.InsuranceCharges=temp[7].cabpiptray
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].cabpiptray/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in pipobjs:
		obj.Discount=temp[0].cabpiptray
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].cabpiptray)/100))
		obj.Freight=temp[1].cabpiptray
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].cabpiptray)/100))
		obj.InterestCOM=temp[2].cabpiptray
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].cabpiptray)/100))
		obj.InwardTax=temp[3].cabpiptray
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].cabpiptray)/100))
		obj.ContigencyPercentage=temp[4].cabpiptray
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].cabpiptray)/100))
		obj.Margin=temp[5].cabpiptray
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].cabpiptray)))
		obj.WarrantyCharges=temp[6].cabpiptray
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].cabpiptray)/100))
		obj.InsuranceCharges=temp[7].cabpiptray
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].cabpiptray/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()
	for obj in traysobjs:
		obj.Discount=temp[0].cabpiptray
		obj.DiscountedPrice=math.ceil(obj.InputPrice-(obj.InputPrice * (temp[0].cabpiptray)/100))
		obj.Freight=temp[1].cabpiptray
		obj.InputCostInclusiveoffreight=math.ceil(obj.DiscountedPrice+(obj.DiscountedPrice * (temp[1].cabpiptray)/100))
		obj.InterestCOM=temp[2].cabpiptray
		obj.UnitCost=math.ceil(obj.InputCostInclusiveoffreight+(obj.InputCostInclusiveoffreight * (temp[2].cabpiptray)/100))
		obj.InwardTax=temp[3].cabpiptray
		obj.UnitCostInclusiveofRisk=math.ceil(obj.UnitCost+(obj.UnitCost * (temp[3].cabpiptray)/100))
		obj.ContigencyPercentage=temp[4].cabpiptray
		obj.UnitCostInclusiveofContigency=math.ceil(obj.UnitCostInclusiveofRisk+(obj.UnitCostInclusiveofRisk* (temp[4].cabpiptray)/100))
		obj.Margin=temp[5].cabpiptray
		obj.Unit_Price=math.ceil(((100*obj.UnitCostInclusiveofContigency)/(100-temp[5].cabpiptray)))
		obj.WarrantyCharges=temp[6].cabpiptray
		obj.UnitPrice=math.ceil(obj.Unit_Price+(obj.Unit_Price * (temp[6].cabpiptray)/100))
		obj.InsuranceCharges=temp[7].cabpiptray
		obj.ListPricewithoutRoundup= math.ceil(obj.UnitPrice+ (obj.UnitPrice* temp[7].cabpiptray/100))
		obj.ListPricewithRoundedup= math.ceil((obj.ListPricewithoutRoundup/50)*50)
		obj.save()

	return JsonResponse({'adg':'jyyj','sr_no':sr_no1})

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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwaregeneral.html',context)
class HardWareGeneralResource(resources.ModelResource):
	class Meta:
		model = HardWareGeneral
def export_hardwaregeneral(request):
	member_resource =HardWareGeneralResource()
	dataset = member_resource.export()
	fname=f"H_FlamencoTech Hardware {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwaregeneralimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareGeneral.objects.all().delete()
		except:
			return redirect('hardwaregeneral')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareGeneral.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwaregeneral')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareipvariant.html',context)
class HardWareIpVariantResource(resources.ModelResource):
	class Meta:
		model = HardWareIpVariant
def export_hardwareipvariant(request):
	member_resource =HardWareIpVariantResource()
	dataset = member_resource.export()
	fname=f"H_IP Variant Sheet {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareipvariantimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareIpVariant.objects.all().delete()
		except:
			return redirect('hardwareipvariant')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareIpVariant.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareipvariant')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareactive.html',context)
class HardWareActiveResource(resources.ModelResource):
	class Meta:
		model = HardWareActive
def export_hardwareactive(request):
	member_resource = HardWareActiveResource()
	dataset = member_resource.export()
	fname=f"H_Active Components {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareactiveimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareActive.objects.all().delete()
		except:
			return redirect('hardwareactive')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareActive.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareactive')
def edithardwareactive(request):
	sr_no=request.POST.get('sr_no')
	t=HardWareActive.objects.get(sr_no=sr_no)
	print(request.POST.get('Qty'))
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarepassive.html',context)
class HardWarePassiveResource(resources.ModelResource):
	class Meta:
		model = HardWarePassive
def export_hardwarepassive(request):
	member_resource =HardWarePassiveResource()
	dataset = member_resource.export()
	fname=f"H_Passive Components {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarepassiveimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWarePassive.objects.all().delete()
		except:
			return redirect('hardwarepassive')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWarePassive.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarepassive')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareethernet.html',context)
class HardWareEthernetResource(resources.ModelResource):
	class Meta:
		model = HardWareEthernet
def export_hardwareethernet(request):
	member_resource =HardWareEthernetResource()
	dataset = member_resource.export()
	fname=f"H_Ethernet Components {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareethernetimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareEthernet.objects.all().delete()
		except:
			return redirect('hardwareethernet')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareEthernet.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareethernet')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareddc.html',context)
class HardWareDdcResource(resources.ModelResource):
	class Meta:
		model = HardWareDdc
def export_hardwareddc(request):
	member_resource =HardWareDdcResource()
	dataset = member_resource.export()
	fname=f"H_DDC Components {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareddcimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareDdc.objects.all().delete()
		except:
			return redirect('hardwareddc')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareDdc.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareddc')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarebmssensors.html',context)
class HardWareBmsSensorsResource(resources.ModelResource):
	class Meta:
		model = HardWareBmsSensors
def export_hardwarebmssensors(request):
	member_resource =HardWareBmsSensorsResource()
	dataset = member_resource.export()
	fname=f"H_BMS Sensors {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarebmssensorsimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareBmsSensors.objects.all().delete()
		except:
			return redirect('hardwarebmssensors')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareBmsSensors.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarebmssensors')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarethirdparty.html',context)
class HardWareThirdPartyResource(resources.ModelResource):
	class Meta:
		model = HardWareThirdParty
def export_hardwarethirdparty(request):
	member_resource =HardWareThirdPartyResource()
	dataset = member_resource.export()
	fname=f"H_Third Party Software {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarethirdpartyimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareThirdParty.objects.all().delete()
		except:
			return redirect('hardwarethirdparty')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareThirdParty.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarethirdparty')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarebmscabling.html',context)
class HardWareBmsScablingResource(resources.ModelResource):
	class Meta:
		model = HardWareBmsScabling
def export_hardwarebmscabling(request):
	member_resource =HardWareBmsScablingResource()
	dataset = member_resource.export()
	fname=f"H_BMS Cabling {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarebmscablingimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareBmsScabling.objects.all().delete()
		except:
			return redirect('hardwarebmscabling')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareBmsScabling.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarebmscabling')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarepiping.html',context)
class HardWarePipingResource(resources.ModelResource):
	class Meta:
		model = HardWarePiping
def export_hardwarepiping(request):
	member_resource =HardWarePipingResource()
	dataset = member_resource.export()
	fname=f"H_Piping {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarepipingimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWarePiping.objects.all().delete()
		except:
			return redirect('hardwarepiping')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWarePiping.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			return redirect('hardwarepiping')  
		return redirect('hardwarepiping')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwaretrays.html',context)
def iandctables(request):
	Pm_Finals=Pm_Final.objects.all()
	Pm_After_Margins=Pm_After_Margin.objects.all()
	Pm_After_Costs=Pm_After_Cost.objects.all()
	print(Pm_Finals)
	print("gg")
	print(Pm_After_Margins)
	print("gg")
	print(Pm_After_Costs)
	print("gg")
	context={'Pm_Finals':Pm_Finals,'Pm_After_Margins':Pm_After_Margins,'Pm_After_Costs':Pm_After_Costs}
	return render(request,'Admin1/iandctables.html',context)
class HardWareTraysResource(resources.ModelResource):
	class Meta:
		model = HardWareTrays
def export_hardwaretrays(request):
	member_resource =HardWareTraysResource()
	dataset = member_resource.export()
	fname=f"H_Trays {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwaretraysimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareTrays.objects.all().delete()
		except:
			return redirect('hardwaretrays')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareTrays.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwaretrays')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwaregeneralinstall.html',context)
class HardWareGeneralInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareGeneralInstall
def export_hardwaregeneralinstall(request):
	member_resource =HardWareGeneralInstallResource()
	dataset = member_resource.export()
	fname=f"FT_Hardware Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwaregeneralinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareGeneralInstall.objects.all().delete()
		except:
			return redirect('hardwaregeneralinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareGeneralInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwaregeneralinstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareipvariantinstall.html',context)
class HardWareIpVariantInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareIpVariantInstall
def export_hardwareipvariantinstall(request):
	member_resource =HardWareIpVariantInstallResource()
	dataset = member_resource.export()
	fname=f"H_IP Variant Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareipvariantinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareIpVariantInstall.objects.all().delete()
		except:
			return redirect('hardwareipvariantinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareIpVariantInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareipvariantinstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareactiveinstall.html',context)
class HardWareActiveInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareActiveInstall
def export_hardwareactiveinstall(request):
	member_resource =HardWareActiveInstallResource()
	dataset = member_resource.export()
	fname=f"H_Active Components Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareactiveinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareActiveInstall.objects.all().delete()
		except:
			return redirect('hardwareactiveinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareActiveInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareactiveinstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarepassiveinstall.html',context)
class HardWarePassiveInstallResource(resources.ModelResource):
	class Meta:
		model =    HardWarePassiveInstall
def export_hardwarepassiveinstall(request):
	member_resource=HardWarePassiveInstallResource()
	dataset = member_resource.export()
	fname=f"H_Passive Components Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarepassiveinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWarePassiveInstall.objects.all().delete()
		except:
			return redirect('hardwarepassiveinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWarePassiveInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarepassiveinstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareethernetinstall.html',context)
class HardWareEthernetInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareEthernetInstall
def export_hardwareethernetinstall(request):
	member_resource =HardWareEthernetInstallResource()
	dataset = member_resource.export()
	fname=f"H_Ethernet_Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareethernetinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareEthernetInstall.objects.all().delete()
		except:
			return redirect('hardwareethernetinstall')
		try:
			for data in imported_data:	
				HardWareEthernetInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareethernetinstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwareddcinstall.html',context)
class HardWareDdcInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareDdcInstall
def export_hardwareddcinstall(request):
	member_resource =HardWareDdcInstallResource()
	dataset = member_resource.export()
	fname=f"H_DDC Components Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwareddcinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareDdcInstall.objects.all().delete()
		except:
			return redirect('hardwareddcinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareDdcInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwareddcinstall')

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
	Pm_Finals=Pm_Final.objects.all()
	Pm_After_Margins=Pm_After_Margin.objects.all()
	Pm_After_Costs=Pm_After_Cost.objects.all()
	context={'Pm_Finals':list(Pm_Finals.values()),'Pm_After_Margins':list(Pm_After_Margins.values()),'Pm_After_Costs':list(Pm_After_Costs.values()),'entries':entries,'Software_Revised_Extras':list(Software_Revised_Extras.values()),'InputConfigurations':list(InputConfigurations.values()),'Automate_Pricings':list(Automate_Pricings.values()),'Desk_Booking_Solutions':list(Desk_Booking_Solutions.values()),'Desk_Utilization_Solutions':list(Desk_Utilization_Solutions.values()),'Desk_Planning_Solutions':list(Desk_Planning_Solutions.values()),'Employee_One_Mobile_Apps':list(Employee_One_Mobile_Apps.values()),'Rosterings':list(Rosterings.values()),'Wayfindings':list(Wayfindings.values()),'Feedbacks':list(Feedbacks.values()),'Kiosk_Licenses':list(Kiosk_Licenses.values()),'Meeting_Room_License_Occupancys':list(Meeting_Room_License_Occupancys.values()),'Meeting_Room_License_People_Counts':list(Meeting_Room_License_People_Counts.values()),'Meeting_Room_License_Bookings':list(Meeting_Room_License_Bookings.values()),'Restroom_License_People_Counts':list(Restroom_License_People_Counts.values()),'Restroom_License_Wet_floor_detections':list(Restroom_License_Wet_floor_detections.values()),'Restroom_License_Odours':list(Restroom_License_Odours.values()),'Human_body_temperature_Licenses':list(Human_body_temperature_Licenses.values())}
#Pm_Finals,Pm_After_Margins,Pm_After_Costs
	
	return render(request,'Admin1/SpazioPriceCalculator.html',context)
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
	
	return render(request,'Admin1/SpazioPriceCalculatoredit.html',context)
class SpazioPriceCalculatorResource(resources.ModelResource):
	class Meta:
		model = SpazioPriceCalculator
def export_SpazioPriceCalculators(request):
	member_resource =SpazioPriceCalculatorResource()
	dataset = member_resource.export()
	fname=f"Spazio Price Calculator {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarebmssensorsinstall.html',context)
class HardWareBmsSensorsInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareBmsSensorsInstall
def export_hardwarebmssensorsinstall(request):
	member_resource =HardWareBmsSensorsInstallResource()
	dataset = member_resource.export()
	fname=f"H_BMS Sensors Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarebmssensorsinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareBmsSensorsInstall.objects.all().delete()
		except:
			return redirect('hardwarebmssensorsinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareBmsSensorsInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarebmssensorsinstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarethirdpartyinstall.html',context)
class HardWareThirdPartyInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareThirdPartyInstall
def export_hardwarethirdpartyinstall(request):
	member_resource =HardWareThirdPartyInstallResource()
	dataset = member_resource.export()
	fname=f"H_Third Party Software Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarethirdpartyinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareThirdPartyInstall.objects.all().delete()
		except:
			return redirect('hardwarethirdpartyinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareThirdPartyInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarethirdpartyinstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarebmscablinginstall.html',context)
class HardWareBmsScablingInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareBmsScablingInstall
def export_hardwarebmscablinginstall(request):
	member_resource =HardWareBmsScablingInstallResource()
	dataset = member_resource.export()
	fname=f"H_BMS Cabling Instal {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarebmscablinginstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareBmsScablingInstall.objects.all().delete()
		except:
			return redirect('hardwarebmscablinginstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareBmsScablingInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarebmscablinginstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwarepipinginstall.html',context)
class HardWarePipingInstallResource(resources.ModelResource):
	class Meta:
		model = HardWarePipingInstall
def export_hardwarepipinginstall(request):
	member_resource =HardWarePipingInstallResource()
	dataset = member_resource.export()
	fname=f"H_Piping Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwarepipinginstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWarePipingInstall.objects.all().delete()
		except:
			return redirect('hardwarepipinginstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWarePipingInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwarepipinginstall')
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
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/hardwaretraysinstall.html',context)
def hardwaremaneffortsinstall(request):
	entries=ManEffortsInstall.objects.all()
	context=fetchdata()
	context['entries']=entries
	return render(request,'Admin1/manefforts.html',context)
class HardWareTraysInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareTraysInstall
def export_hardwaretraysinstall(request):
	member_resource =HardWareTraysInstallResource()
	dataset = member_resource.export()
	fname=f"H_Trays Install {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def hardwaretraysinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			HardWareTraysInstall.objects.all().delete()
		except:
			return redirect('hardwaretraysinstall')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				HardWareTraysInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwaretraysinstall')
class HardWareManEfforts(resources.ModelResource):
	class Meta:
		model = ManEffortsInstall
def export_maneffortsinstall(request):
	member_resource =HardWareManEfforts()
	dataset = member_resource.export()
	fname=f"FT Efforts Man Days {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def maneffortsinstallimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			ManEffortsInstall.objects.all().delete()
		except:
			return redirect('hardwaremaneffortsinstall')
		try:
			for data in imported_data:
				print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				ManEffortsInstall.objects.create(sr_no=int(data[0]),MakeBrand=data[1],Model=data[2],InstallationEquipments=data[3],UnitDescription=data[4],Qty=int(data[5]),InputPrice=int(data[6]),Discount=int(data[7]),DiscountedPrice=int(data[8]),Freight=int(data[9]),InputCostInclusiveoffreight=int(data[10]),InterestCOM=int(data[11]),UnitCost=int(data[12]),InwardTax=int(data[13]),UnitCostInclusiveofRisk=int(data[14]),ContigencyPercentage=int(data[15]),UnitCostInclusiveofContigency=int(data[16]),Margin=int(data[17]),Unit_Price=int(data[18]),WarrantyCharges=int(data[19]),UnitPrice=int(data[20]),InsuranceCharges=int(data[21]),ListPricewithoutRoundup=int(data[22]),ListPricewithRoundedup=int(data[23]))
		except:
			print("errored")
			pass    
		return redirect('hardwaremaneffortsinstall')
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
def editmaneffortsinstall(request):
	sr_no=request.POST.get('sr_no')
	t=ManEffortsInstall.objects.get(sr_no=sr_no)
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
def automatepricing(request):
	entries=Automate_Pricing.objects.all()
	return render(request,'Admin1/automatepricing.html',context={'entries':entries})
class Automate_PricingResource(resources.ModelResource):
	class Meta:
		model = Automate_Pricing
def export_automatepricing(request):
	member_resource =Automate_PricingResource()
	dataset = member_resource.export()
	fname=f"member-data {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def automatepricingimport(request):
	if request.method == 'POST':
		dataset = Dataset()
		new_persons = request.FILES['bookfile']
		try:
			imported_data = dataset.load(new_persons.read(),format='xls')
			Automate_Pricing.objects.all().delete()
		except:
			return redirect('automatepricing')
		try:
			for data in imported_data:
				#print(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24])
				#BookDetails.objects.create(relid=data[0],book_name=data[1])	
				Automate_Pricing.objects.create(sr_no=int(data[0]),Model_No=data[1],Max_Slab=int(data[2]),Pack_Desc=data[3],Inr_Basic=int(data[4]),Inr_Basic_Per_Kpi=int(data[5]),Inr_Premium=int(data[6]),Inr_Premium_Per_Kpi=int(data[7]),Usd_Basic=int(data[8]),Usd_Premium=int(data[9]))
		except:
			print("errored")
			pass    
		return redirect('automatepricing')

def editDBS(request):
	sr_no=request.POST.get('sr_no')
	t=Desk_Booking_Solution.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 


def editDPS(request):
	 
	sr_no=request.POST.get('sr_no')
	t=Desk_Planning_Solution.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editDUS(request):
	sr_no=request.POST.get('sr_no')
	t=Desk_Utilization_Solution.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editEOMA(request):
	sr_no=request.POST.get('sr_no')
	t=Employee_One_Mobile_App.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editRost(request):
	sr_no=request.POST.get('sr_no')
	t=Rostering.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editWF(request):
	sr_no=request.POST.get('sr_no')
	t=Wayfinding.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editFB(request):
	sr_no=request.POST.get('sr_no')
	t=Feedback.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editKL(request):
	sr_no=request.POST.get('sr_no')
	t=Kiosk_License.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editMRLO(request):
	sr_no=request.POST.get('sr_no')
	t=Meeting_Room_License_Occupancy.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',})
 #                    
def editMRLPC(request):
	sr_no=request.POST.get('sr_no')
	t=Meeting_Room_License_People_Count.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editMRLB(request):
	sr_no=request.POST.get('sr_no')
	t=Meeting_Room_License_Booking.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 



def editRLPC(request):
	sr_no=request.POST.get('sr_no')
	t=Restroom_License_People_Count.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editRLWFT(request):
	sr_no=request.POST.get('sr_no')
	t=Restroom_License_Wet_floor_detection.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editRLO(request):
	sr_no=request.POST.get('sr_no')
	t=Restroom_License_Odour.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editHBTL(request):
	sr_no=request.POST.get('sr_no')
	t=Human_body_temperature_License.objects.get(sr_no=sr_no)
	t.Packs_Slabs=request.POST.get('Packs_Slabs')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Rate=request.POST.get('Rate')
	t.Total_Quantity=request.POST.get('Total_Quantity')
	t.Volume=request.POST.get('Volume')
	t.Rate_Per_Slab=request.POST.get('Rate_Per_Slab')
	t.Total=request.POST.get('Total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editautomate(request):
	sr_no=request.POST.get('sr_no')
	t=Automate_Pricing.objects.get(sr_no=sr_no)
	t.Model_No=request.POST.get('Model_No')
	t.Max_Slab=request.POST.get('Max_Slab')
	t.Pack_Desc=request.POST.get('Pack_Desc')
	t.Inr_Basic=request.POST.get('Inr_Basic')
	t.Inr_Basic_Per_Kpi=request.POST.get('Inr_Basic_Per_Kpi')
	t.Inr_Premium=request.POST.get('Inr_Premium')
	t.Inr_Premium_Per_Kpi=request.POST.get('Inr_Premium_Per_Kpi')
	t.Usd_Basic=request.POST.get('Usd_Basic')
	t.Usd_Premium=request.POST.get('Usd_Premium')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 


class HardWareActiveResource(resources.ModelResource):
	class Meta:
		model = HardWareActive
def export_hardwareactive(request):
	member_resource = HardWareActiveResource()
	dataset = member_resource.export()
	fname=f"member-data {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
#,,
def editPm_Final(request):
	sr_no=request.POST.get('sr_no')
	t=Pm_Final.objects.get(sr_no=sr_no)
	t.minslab=request.POST.get('minslab')
	t.maxslab=request.POST.get('maxslab')
	t.rate=request.POST.get('rate')
	t.total=request.POST.get('total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editPm_Margin(request):
	sr_no=request.POST.get('sr_no')
	t=Pm_After_Margin.objects.get(sr_no=sr_no)
	t.minslab=request.POST.get('minslab')
	t.maxslab=request.POST.get('maxslab')
	t.rate=request.POST.get('rate')
	t.total=request.POST.get('total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
def editPm_Cost(request):
	sr_no=request.POST.get('sr_no')
	t=Pm_After_Cost.objects.get(sr_no=sr_no)
	t.minslab=request.POST.get('minslab')
	t.maxslab=request.POST.get('maxslab')
	t.rate=request.POST.get('rate')
	t.total=request.POST.get('total')
	t.save()
	return JsonResponse({'adg':'jyyj',}) 
	 
	
	
	
	
######################


			  
					
					
					
					
# , ,

def edit_quot_admin(request,ref_no):
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
	return render(request, 'Admin1/clientdetailsedit.html', {'data': dataJSON})
def createquotation(request):
	return render(request,'Admin1/clientdetails.html')

