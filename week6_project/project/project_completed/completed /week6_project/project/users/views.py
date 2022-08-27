
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .forms import Register_form
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
# from django.template import RequestContext



from django.views.decorators.cache import cache_control





def home(request):
    if 'user' in request.session:
        return render(request,'home.html',{})
    # else:
    #     return redirect('users:login')


# register section 

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
                messages.info(request,'User Name Taken')
                return redirect('users:register')
            elif User.objects.filter(email=email):                       # here we are comparing the passwords( form database with locally inputted )
                messages.info(request,'Email Id Taken')
                return redirect('users:register')
            else: 
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password= password1)
                user.save();                                              # here we are actually inserting user details to the a table which is automatically created by django during the migration "User"
                messages.success(request,'User Successfully Created')
                return redirect('users:login')                                 # after successful register an account we should redirect back to login page.
        else:
            messages.info(request,'Password Not Matching')
            return redirect('users:register')
        #return redirect('/') 
    else:
        return render(request,'register.html',{})



def local_admin(request):
    user= request.user
    if user.is_superuser :                                      # check whether the user is a super user  
        return redirect('users:main_admin')
    else: 
        return redirect('/')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'user' in request.session:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')       # getting the user detail form the user. 
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)  # if the same username and password exist this object will be created or else it will be none.
            if user is not None :                                           # check if the object is created
                request.session['user'] = username
                print("True")
                auth.login(request,user)                               # we are giving access to the user. 
                return redirect('/')                                   # redirect to normal user space                                                              
            else: 
                messages.info(request,'Invalid Credentials')                # if the login fail. 
                return redirect('users:login')                                    # redirect to the same page 
        else :
            return render(request, 'login.html',{})
    


def logout(request): 
    auth.logout(request)
    return redirect('users:login') # redirect to home page.



def main_admin(request):
    user= request.user
    if user.is_superuser:
        context = User.objects.all().order_by('id')      
        return render(request, 'main_admin.html',{'context':context})
    else:
        return redirect('users:login')



def edit_user(request,id):
    user= request.user
    if user.is_superuser:
        add_user = User.objects.get(id=id)
        form = Register_form(request.POST or None, instance=add_user)
        if form.is_valid():
            form.save()
            return redirect('users:main_admin')
        return render(request, 'edit_user.html',{'form':form , 'add_user':add_user})
    else:
        return redirect('users:login')




def delete_user(request,id):
    user= request.user
    if user.is_superuser:
        User.objects.filter(id=id).delete()
        return redirect('users:main_admin')
    else:
        return redirect('users:login')



def add_user(request):
    user= request.user
    if user.is_superuser:   
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
                    messages.info(request,'User Name Taken')
                    return redirect('users:register')
                elif User.objects.filter(email=email):                       # here we are comparing the passwords( form database with locally inputted )
                    messages.info(request,'Email Id Taken')
                    return redirect('users:register')
                else: 
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password= password1)
                    user.save()                                              # here we are actually inserting user details to the a table which is automatically created by django during the migration "User"                     # to print a message a user is successfully created 
                    messages.success(request,'User Successfully Created')
                    return redirect('users:main_admin')                                 # after successful register an account we should redirect back to login page.
            else:
                messages.info(request,'Password Not Matching')   
                return redirect('users:register')
            # return redirect('/') 
        else:
            return render(request,'register.html',{})
    else:
        return redirect('users:login')



def search_user(request):
    user= request.user
    if user.is_superuser:
        users=None
        query=None
        if 'q' in request.GET:
            query=request.GET.get('q')
            users=User.objects.all().filter(Q(first_name__contains=query) | Q(last_name__contains=query) | Q(email__contains=query) | Q(username__contains=query))
            return render(request,'search.html', {'query': query, 'context': users})
    else:
        return redirect('users:login')
        
















































# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.db.models import Q
# from .forms import Register_form
# from django.contrib.auth.models import User
# from django.contrib.auth.models import auth
# # from django.template import RequestContext



# from django.views.decorators.cache import cache_control

# def home(request):
#     return render(request,'home.html',{})

# # register section 

# def register(request):
     
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')                      # this should be same name which is used in html 'name' field 
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         email = request.POST.get('email')     
#                                                                          # validations to performs 
#                                                                          # 1 password 1 matches with password 2 
#         if password1 == password2:
#                                                                          # 2  username and email id used by current database or not  ( these two are unique field )
#             if User.objects.filter(username=username):                   # here we are comparing the username of database with new user name. 
#                 messages.info(request,'User Name Taken')
#                 return redirect('users:register')
#             elif User.objects.filter(email=email):                       # here we are comparing the passwords( form database with locally inputted )
#                 messages.info(request,'Email Id Taken')
#                 return redirect('users:register')
#             else: 
#                 user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password= password1)
#                 user.save();                                              # here we are actually inserting user details to the a table which is automatically created by django during the migration "User"
#                 messages.success(request,'User Successfully Created')
#                 return redirect('users:login')                                 # after successful register an account we should redirect back to login page.
#         else:
#             messages.info(request,'Password Not Matching')
#             return redirect('users:register')
#         #return redirect('/') 
#     else:
#         return render(request,'register.html',{})


# def local_admin(request):
#     user= request.user
#     if user.is_superuser :                                      # check whether the user is a super user  
#         return redirect('users:main_admin')


# def login(request):
    
#     if request.method == 'POST':
#         username = request.POST.get('username')       # getting the user detail form the user. 
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)  # if the same username and password exist this object will be created or else it will be none.
#         if user is not None :                                           # check if the object is created
#             auth.login(request,user)                               # we are giving access to the user. 
#             return redirect('/')                                   # redirect to normal user space                                                              
#         else: 
#             messages.info(request,'Invalid Credentials')                # if the login fail. 
#             return redirect('users:login')                                    # redirect to the same page 
#     else :
#         return render(request, 'login.html',{})


# def logout(request): 
#     auth.logout(request)
#     return redirect('users:login') # redirect to home page.


# def main_admin(request):
#     user= request.user
#     if user.is_superuser:
#         context = User.objects.all().order_by('id')      
#         return render(request, 'main_admin.html',{'context':context})
#     else:
#         return redirect('users:login')


# def edit_user(request,id):
#     user= request.user
#     if user.is_superuser:
#         add_user = User.objects.get(id=id)
#         form = Register_form(request.POST or None, instance=add_user)
#         if form.is_valid():
#             form.save()
#             return redirect('users:main_admin')
#         return render(request, 'edit_user.html',{'form':form , 'add_user':add_user})
#     else:
#         return redirect('users:login')


# def delete_user(request,id):
#     user= request.user
#     if user.is_superuser:
#         User.objects.filter(id=id).delete()
#         return redirect('users:main_admin')
#     else:
#         return redirect('users:login')


# def add_user(request):
#     user= request.user
#     if user.is_superuser:   
#         if request.method == 'POST':
#             first_name = request.POST.get('first_name')                      # this should be same name which is used in html 'name' field 
#             last_name = request.POST.get('last_name')
#             username = request.POST.get('username')
#             password1 = request.POST.get('password1')
#             password2 = request.POST.get('password2')
#             email = request.POST.get('email')     
#                                                                             # validations to performs 
#                                                                             # 1 password 1 matches with password 2 
#             if password1 == password2:
#                                                                             # 2  username and email id used by current database or not  ( these two are unique field )
#                 if User.objects.filter(username=username):                   # here we are comparing the username of database with new user name. 
#                     messages.info(request,'User Name Taken')
#                     return redirect('users:register')
#                 elif User.objects.filter(email=email):                       # here we are comparing the passwords( form database with locally inputted )
#                     messages.info(request,'Email Id Taken')
#                     return redirect('users:register')
#                 else: 
#                     user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password= password1)
#                     user.save()                                              # here we are actually inserting user details to the a table which is automatically created by django during the migration "User"                     # to print a message a user is successfully created 
#                     messages.success(request,'User Successfully Created')
#                     return redirect('users:main_admin')                                 # after successful register an account we should redirect back to login page.
#             else:
#                 messages.info(request,'Password Not Matching')   
#                 return redirect('users:register')
#             # return redirect('/') 
#         else:
#             return render(request,'register.html',{})
#     else:
#         return redirect('users:login')


# def search_user(request):
#     user= request.user
#     if user.is_superuser:
#         users=None
#         query=None
#         if 'q' in request.GET:
#             query=request.GET.get('q')
#             users=User.objects.all().filter(Q(first_name__contains=query) | Q(last_name__contains=query) | Q(email__contains=query) | Q(username__contains=query))
#             return render(request,'search.html', {'query': query, 'context': users})
#     else:
#         return redirect('users:login')
        








