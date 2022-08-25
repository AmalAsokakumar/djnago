from django.urls import path
from . import views 

app_name = 'users'
urlpatterns = [ 
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('admin/',views.main_admin, name='main_admin'),
    path('edit/<int:id>',views.edit_user, name='edit_user'),
    path('search/',views.search_user, name='search_user'),
    path('delete/<int:id>',views.delete_user, name='delete_user'),
    path('add_user/',views.add_user, name='add_user'),
    path('admin/home/',views.home, name='home_user'),
    path('local_admin/',views.local_admin, name='local_admin')
]
