# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.models import UserCreationForm

# class RegisterForm(UserCreationForm):
    
#     email= forms.EmailField(
#         max_length= 100,
#         required= True,
#         help_text = 'Enter Email Address',
#         widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),
#         ),
#     first_name= forms.CharField(
#         max_length= 100,
#         required= True,
#         help_text= 'Enter First Name',
#         widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
#         ),
#     last_name= forms.CharField(
#         max_length= 100, 
#         required= True, 
#         help_text= 'Enter Last Name',
#         widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
#         ),
#     username= forms.CharField(
#         max_length= 100,
#         required= True,
#         help_text='Enter User Name',
#         widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'User Name'}),
#         ),
#     password= forms.CharField(
#         max_length= 100,
#         required= True,
#         help_text= 'Enter Password',
#         widget = forms.TextInput(attrs= {'class': 'form-control','placeholder':'password'}), 
#         ),
#     password2= forms.CharField(
#         max_length= 100,
#         required= True,
#         help_text='Enter Password',
#         widget= forms.TextInput(attrs= {'class': 'form-control','placeholder':'password Again'}), 
#         )
    
#     check= forms.BooleanField(Required=True)
    
    
    # class Meta:
    #     model= User
    #     fields= ['username','email','first_name','last_name','password','password2','check']
    
    