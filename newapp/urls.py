from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sidebar-left.html', views.daneshjo1, name='daneshjo1'),
    path('sidebar-right.html', views.vahed, name='vahed'),
    path('basic-grid.html', views.info_dars1, name='info_dars1'),
]
'''path('daneshjo/', views.daneshjo1, name='daneshjo1'),
    path('info_dars/', views.info_dars1, name='info_dars1'),
    path('', views.home, name='home'),'''
#path('index/', views.index, name='index'),
#path('info_dars/', views.info_dars1, name='info_dars1'),
# path('daneshjo/', views.daneshjo1, name='daneshjo1'), 
#path('daneshjo/', views.daneshjo1, name='daneshjo1'),

#'daneshjo/'
