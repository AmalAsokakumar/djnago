from django.urls import path
from . import views 

urlpatterns = [ 
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('admin/',views.main_admin, name='main_admin'),
    path('edit/<int:id>',views.edit_user, name='edit_user'),
    path('delete/<int:id>',views.delete_user, name='delete_user'),
]
