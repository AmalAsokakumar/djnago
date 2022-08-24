from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import RegisterForm
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name') # this should be same name which is used in html name field 
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password= password1)
        user.save() 
        #print('user created successfully') # to print a message a user is successfully created 
        return redirect('/')# this should be the name that we use to reach    home  >  ('/')
        
    else:
        pass
    return render(request, 'register.html', {})


# # Create your views here.
# def register(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         context= {'form':form}
#         return render(request, 'register.html', context)
#     if request.method == 'POST':
#         form= RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user=form.cleaned_data.get('username')
#             messages.success(request,'Account was created for '+ user)
#             return redirect('home_page')
#         else: 
#             print('Form is not valid')
#             messages.error(request, 'Error Processing Your Request')
#             context = {'form':form}
#             return render(request, 'register.html', context)
#     return render(request, 'register.html', {})