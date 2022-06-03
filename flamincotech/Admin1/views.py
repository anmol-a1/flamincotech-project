from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
def index(request):
    return render(request,'Admin1/index.html')
def registeruser(request):
    return render(request,'Admin1/registeruser.html')
def history(request):
    return render(request,'Admin1/history.html')
def trackp(request):
    return render(request,'Admin1/trackp.html')
# Create your views here.
