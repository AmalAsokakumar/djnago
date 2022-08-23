import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    date = datetime.datetime.now().date()
    # return render(request, 'index.html',{'data':date})
    days_of_week = ['mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return render(request,'index.html',{'date': date , "days_of_week" : days_of_week})
    
def form(request):
    if request.method == 'GET':
        return render(request,'form.html',{})
        
    elif request.method == 'POST': 
        text= request.POST['text']
        email = request.POST['email']
        data = [text, email]
        return render(request,'result.html',{'data': data})
    
    
    
def result(request):
    pass                                                                                                      