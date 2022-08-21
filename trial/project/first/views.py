from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    
    data =' hai this is my test project '
    # return HttpResponse('HELLOWORLD')
    return render(request, 'index.html',{'data':data})


# # simple form creation 
# def form(request):
#     if request.method == 'GET':
#         return render(request,'forms.html')
#     if request.method == 'POST':
#        text= request.POST.get('text')
#        return render(request, '',{'data':text})   # here the returning request is kind http://127.0.0.1:8000/forms/form
# # here it is looking for a url forms/form