from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import InputConfiguration
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
def editconfiguration(request):
    print("s")
    print("ugugui")
    sr_no=request.POST.get('sr_no')
    print(sr_no)
    if True:
        print("hhh")
    return JsonResponse({'adg':'jyyj'})
# Create your views here.
