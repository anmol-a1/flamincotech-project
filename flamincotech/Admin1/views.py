from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import InputConfiguration
=======
from django.http import HttpResponseRedirect,HttpResponse
from .models import InputConfiguration,vpss
>>>>>>> 0adad1851ba7c444700ed4cce46b05b24810f456
def index(request):
    return render(request,'Admin1/index.html')
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
<<<<<<< HEAD
def editconfiguration(request):
    print("s")
    print("ugugui")
    sr_no=request.POST.get('sr_no')
    print(sr_no)
    if True:
        print("hhh")
    return JsonResponse({'adg':'jyyj'})
=======
def vpss(request):
    entries=vpss.objects.all()
    context={'entries':entries}
    return render(request,'Admin1/vpss.html',context)
>>>>>>> 0adad1851ba7c444700ed4cce46b05b24810f456
# Create your views here.
