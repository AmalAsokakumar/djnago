from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import RegisterForm
from django.contrib.auth.models import User, auth



def register(request):
    
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')                      # this should be same name which is used in html 'name' field 
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')     
                                                                         # validations to performs 
                                                                         # 1 password 1 matches with password 2 
        if password1 == password2:
                                                                         # 2  username and email id used by current database or not  ( these two are unique field )
            if User.objects.filter(username=username):                   # here we are comparing the username of database with new user name. 
                #print("user name taken ")
                messages.info(request,'User Name Taken')
            elif User.objects.filter(email=email):                       # here we are comparing the passwords( form database with locally inputted )
                # print("Email id is taken")
                messages.info(request,'Email Id Taken')
            else: 
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password= password1)
                user.save()                                              # here we are actually inserting user details to the a table which is automatically created by django during the migration "User"
                #print('user created successfully')                      # to print a message a user is successfully created 
                messages.success(request,'User Successfully Created')
                return redirect('login')                                 # after successful register an account we should redirect back to login page.
        else:
            messages.info(request,'Password Not Matching')
            # print('password not matching ')       
    else:
        
        return render(request, 'register.html',{})
        # return render(request,'register')





def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)  # if the same username and password exist this object will be created or else it will be none.
        if user is not None :                                           # check if the object is created
            if user.is_superuser :                                      # check whether the user is a super user 
                auth.login(request,user)                                # we are giving access to the user. 
                return redirect('/')                                    # super user admin panel address 
            else:
                 auth.login(request,user)                               # we are giving access to the user. 
                 return redirect('/')                                   # redirect to normal user space 
                                                                        # i have to edit this section and add another checking to find superuser  
        else: 
            messages.info(request,'Invalid Credentials')                # if the login fail. 
            return redirect('login')                                    # redirect to the same page 
    else :
        return render(request, 'login.html',{})

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



