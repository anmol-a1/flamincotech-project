from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
def index(request):
    return render(request,'User/index.html')
def createquotation(request):
    return render(request,'User/clientdetails.html')
def history(request):
    return render(request,'User/history.html')
