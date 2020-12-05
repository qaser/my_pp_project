from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='oil_index'),
    path('pumps/', views.pump_list, name='pump_site'),
    path('add-pump/', views.add_pump, name='add_pump'),
    path('add-util/', views.add_util, name='add_util'),
    path('add-filterchange/', views.add_filterchange, name='add_filterchange')
]
