from django.shortcuts import render,redirect
import json
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import IandC,NewUser,Software_Revised_Extra,Automate_Pricing,InputConfiguration,vpss,HardWareGeneral,HardWareIpVariant,HardWareActive,HardWarePassive,HardWareEthernet,HardWareDdc,HardWareBmsSensors,HardWareThirdParty,HardWareBmsScabling,HardWarePiping,HardWareTrays,HardWareGeneralInstall,HardWareIpVariantInstall,HardWareActiveInstall,HardWarePassiveInstall,HardWareEthernetInstall,HardWareDdcInstall,HardWareBmsSensorsInstall,HardWareThirdPartyInstall,HardWareBmsScablingInstall,HardWarePipingInstall,HardWareTraysInstall,SpazioPriceCalculator,Desk_Booking_Solution,Desk_Utilization_Solution,Desk_Planning_Solution,Employee_One_Mobile_App,Rostering,Wayfinding,Feedback,Kiosk_License,Meeting_Room_License_Occupancy,Meeting_Room_License_People_Count,Meeting_Room_License_Booking,Restroom_License_People_Count,Restroom_License_Wet_floor_detection,Restroom_License_Odour ,Human_body_temperature_License
from User.models import Soft_Items,Bms_Trays,Bms_Piping,Bms_Cabling,Bms_Sensors,Ddc,Ethernet,Fiber,Active,General
import datetime
from import_export import resources
import tablib
from tablib import Dataset
def fetchdata():
	context={}
	InputConfigurations=InputConfiguration.objects.all()
	for i in range(len(InputConfigurations)):
		context[f"InputConfigurations{i+1}"]=InputConfigurations[i]
	return context
def iandc(request):
	entries=IandC.objects.all()
	context={'entries':entries}
	return render(request,'Admin1/iandc.html',context)
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
	fname=f"member-data {datetime.datetime.now().date()}"
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = f'attachment; filename={fname}.xls'
	return response
def history(request):
	return render(request,'Admin1/history.html')
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
	return render(request,'Admin1/trackp.html')
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
				InputConfiguration.objects.create(sr_no=int(data[0]),desc=data[1],ft_hardware=int(data[2]),active=int(data[3]),passive=int(data[4]),ddcsensor=int(data[5]),thirdparty=int(data[6]),cabpiptray=int(data[7]),ft_hardware1=int(data[8]),active1=int(data[9]),passive1=int(data[10]),ddcsensor1=int(data[11]),thirdparty1=int(data[12]),cabpiptray1=int(data[13]),ftmandayeffort=int(data[14]),othersmicffort=int(data[15]),ft2=int(data[16]),ft3=int(data[17]),ft4=int(data[18]))
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
class HardWareTraysResource(resources.ModelResource):
	class Meta:
		model = HardWareTrays
def export_hardwaretrays(request):
	member_resource =HardWareTraysResource()
	dataset = member_resource.export()
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	context={'entries':entries,'Software_Revised_Extras':list(Software_Revised_Extras.values()),'InputConfigurations':list(InputConfigurations.values()),'Automate_Pricings':list(Automate_Pricings.values()),'Desk_Booking_Solutions':list(Desk_Booking_Solutions.values()),'Desk_Utilization_Solutions':list(Desk_Utilization_Solutions.values()),'Desk_Planning_Solutions':list(Desk_Planning_Solutions.values()),'Employee_One_Mobile_Apps':list(Employee_One_Mobile_Apps.values()),'Rosterings':list(Rosterings.values()),'Wayfindings':list(Wayfindings.values()),'Feedbacks':list(Feedbacks.values()),'Kiosk_Licenses':list(Kiosk_Licenses.values()),'Meeting_Room_License_Occupancys':list(Meeting_Room_License_Occupancys.values()),'Meeting_Room_License_People_Counts':list(Meeting_Room_License_People_Counts.values()),'Meeting_Room_License_Bookings':list(Meeting_Room_License_Bookings.values()),'Restroom_License_People_Counts':list(Restroom_License_People_Counts.values()),'Restroom_License_Wet_floor_detections':list(Restroom_License_Wet_floor_detections.values()),'Restroom_License_Odours':list(Restroom_License_Odours.values()),'Human_body_temperature_Licenses':list(Human_body_temperature_Licenses.values())}
	
	return render(request,'Admin1/SpazioPriceCalculator.html',context)
class SpazioPriceCalculatorResource(resources.ModelResource):
	class Meta:
		model = SpazioPriceCalculator
def export_SpazioPriceCalculators(request):
	member_resource =SpazioPriceCalculatorResource()
	dataset = member_resource.export()
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
	fname=f"member-data {datetime.datetime.now().date()}"
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
class HardWareTraysInstallResource(resources.ModelResource):
	class Meta:
		model = HardWareTraysInstall
def export_hardwaretraysinstall(request):
	member_resource =HardWareTraysInstallResource()
	dataset = member_resource.export()
	fname=f"member-data {datetime.datetime.now().date()}"
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
			  
					
					
					
					
# , ,