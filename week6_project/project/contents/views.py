from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import destination



def index(request):
    
    dests = destination.objects.all()
    print(destination.objects.all().filter(pk=1))
    # print(dests.desc)
    # print('@'*1000)
    return render(request,'index.html', {'dests':dests})


















# Create your views here.
# def home(request):
#     if request.method == 'GET':
#         return render(request, 'index.html',{})
#     else:
#         username = request.POST['username']
#         password = request.POST['password']
#         userdata = [username, password]
#         #return HttpResponse('YOU HAVE SUCCESSFULLY REGISTERED')
#         return render(request,'test.html', {'userdata': userdata}) #for testing whether the password is properly passing  

# def index(request): 
#     dest = destination() # here we are creating an object for destination model.
#     dest2 = destination()
#     dest3 = destination()
#     dest4 = destination()
#     dest.name= 'patazhi'
#     dest.desc = 'nothing special here'
    
#     dest2.name= 'patazhi'
#     dest2.desc = 'nothing special here'
#     dest3.name= 'patazhi'
#     dest3.desc = 'nothing special here'
#     dest4.name= 'patazhi'
#     dest4.desc = 'nothing special here'
    
#     dests =[ dest, dest2, dest3, dest4]
    
#     return render(request,'index.html',{'dests': dests})
    