from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('particular/', views.retrive),
    path('studcreate/',views.s_create),
    path('markcreate/',views.m_create),
    path('create_update/',views.create_update),
    path('create_update1/', views.create_update1),
    path('create_all/', views.create_all),
    
    path('allstudentmarks/', views.allstudentmarks),
    
    path('updateallmarks/',views.updateallmarks),
    path('deletemarks/',views.deletemarks),
	path('deletestud/',views.deletestud),
    
    path('export_stud_csv/', csrf_exempt(views.export_stud_csv)),

]