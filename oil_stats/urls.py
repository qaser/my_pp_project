from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='oil_index'),
    path('graphs/', views.PumpGraphView.as_view(), name='graphs'),
    path('pumps/', views.PumpListView.as_view(), name='pump_site'),
    path('utils/', views.UtilListView.as_view(), name='util_site'),
    path('strainers/', views.StrainerListView.as_view(), name='strainer_site'),
    path('add-pump/', views.add_pump, name='add_pump'),
    path('add-util/', views.add_util, name='add_util'),
    path('add-strainer-change/', views.add_strainer_change, name='add_strainer_change'),
]
